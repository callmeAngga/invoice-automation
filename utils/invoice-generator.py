import os
import json
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from datetime import datetime
from dummy import dummy_data

def format_currency(amount):
    """Format angka menjadi format mata uang Indonesia"""
    return f"{amount:,.0f}".replace(",", ".")

def format_date(date_str):
    """Format tanggal dari YYYY-MM-DD ke DD-MMM-YYYY"""
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    months = {
        1: "Jan", 2: "Feb", 3: "Mar", 4: "Apr", 5: "May", 6: "Jun",
        7: "Jul", 8: "Aug", 9: "Sep", 10: "Oct", 11: "Nov", 12: "Dec"
    }
    return f"{date_obj.day}-{months[date_obj.month]}-{date_obj.year}"

def calculate_tax(subtotal, tax_rate=0.11):
    """Hitung PPN"""
    return subtotal * tax_rate

def generate_invoice_pdf(invoice_data, filename):
    """Generate PDF invoice dari data JSON"""
    
    # Setup dokumen
    doc = SimpleDocTemplate(filename, pagesize=A4, topMargin=0.5*inch)
    styles = getSampleStyleSheet()
    story = []
    
    # Style custom
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=16,
        spaceAfter=30,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    header_style = ParagraphStyle(
        'CustomHeader',
        parent=styles['Normal'],
        fontSize=12,
        spaceAfter=6,
        alignment=TA_LEFT,
        fontName='Helvetica-Bold'
    )
    
    normal_style = ParagraphStyle(
        'CustomNormal',
        parent=styles['Normal'],
        fontSize=10,
        spaceAfter=6,
        alignment=TA_LEFT
    )
    
    # Header invoice
    title = Paragraph(f"INVOICE {invoice_data['vendor']['name'].upper()}", title_style)
    story.append(title)
    story.append(Spacer(1, 12))
    
    # Informasi invoice
    info_data = [
        ['No. Invoice:', invoice_data['invoice_number']],
        ['Tanggal:', format_date(invoice_data['invoice_date'])],
        ['PO Number:', invoice_data['po_number']],
        ['Vendor:', f"{invoice_data['vendor']['code']} ({invoice_data['vendor']['name']})"],
        ['NPWP:', invoice_data['vendor']['tax_id']]
    ]
    
    info_table = Table(info_data, colWidths=[2*inch, 4*inch])
    info_table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('ALIGN', (0, 0), (0, -1), 'LEFT'),
        ('ALIGN', (1, 0), (1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ]))
    
    story.append(info_table)
    story.append(Spacer(1, 20))
    
    # Tabel items
    table_data = [['Deskripsi', 'Qty', 'Satuan', 'Harga', 'Total']]
    
    subtotal = 0
    for item in invoice_data['items']:
        table_data.append([
            item['description'],
            str(item['quantity']),
            item['unit'],
            format_currency(item['unit_price']),
            format_currency(item['total'])
        ])
        subtotal += item['total']
    
    # Create table
    item_table = Table(table_data, colWidths=[2.5*inch, 0.7*inch, 0.8*inch, 1.2*inch, 1.3*inch])
    item_table.setStyle(TableStyle([
        # Header styling
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        
        # Data rows styling
        ('ALIGN', (0, 1), (0, -1), 'LEFT'),    # Description
        ('ALIGN', (1, 1), (1, -1), 'CENTER'),  # Qty
        ('ALIGN', (2, 1), (2, -1), 'CENTER'),  # Unit
        ('ALIGN', (3, 1), (3, -1), 'RIGHT'),   # Price
        ('ALIGN', (4, 1), (4, -1), 'RIGHT'),   # Total
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.lightgrey]),
        
        # Grid
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 1), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
    ]))
    
    story.append(item_table)
    story.append(Spacer(1, 20))
    
    # Summary
    ppn = calculate_tax(subtotal)
    total = subtotal + ppn
    
    summary_data = [
        ['Subtotal:', format_currency(subtotal)],
        ['PPN (11%):', format_currency(ppn)],
        ['Total:', format_currency(total)]
    ]
    
    summary_table = Table(summary_data, colWidths=[4*inch, 2*inch])
    summary_table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('ALIGN', (0, 0), (0, -1), 'RIGHT'),
        ('ALIGN', (1, 0), (1, -1), 'RIGHT'),
        ('FONTNAME', (0, 2), (1, 2), 'Helvetica-Bold'),  
        ('FONTSIZE', (0, 2), (1, 2), 12),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('LINEABOVE', (0, 2), (-1, 2), 1, colors.black),  
    ]))
    
    story.append(summary_table)
    story.append(Spacer(1, 20))
    
    # Build PDF
    doc.build(story)
    print(f"Invoice PDF berhasil dibuat: {filename}")

# Main function
def main():
    """Generate PDF untuk semua data dummy"""
    print("=== INVOICE PDF GENERATOR ===")

    # Buat folder output
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    print(f"Membuat {len(dummy_data)} invoice PDF...\n")
    
    for i, invoice in enumerate(dummy_data, 1):
        filename = os.path.join(output_dir, f"invoice_{invoice['invoice_number']}.pdf")
        generate_invoice_pdf(invoice, filename)
        print(f"{i}. {filename} - {invoice['vendor']['name']}")
    
    print("\nSemua invoice PDF berhasil dibuat!")
    print("\n=== DATA DUMMY (JSON FORMAT) ===")
    print(json.dumps(dummy_data, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()