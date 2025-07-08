dummy_data = [
    # Valid Invoice 1 - Office Supplies
    {
        "invoice_number": "INV-2025-001",
        "invoice_date": "2025-07-10",
        "vendor": {
            "name": "PT. Supplier Jaya",
            "code": "VEN-1001",
            "tax_id": "01.234.567.8-912.000"
        },
        "items": [
            {
                "description": "Kertas A4 80gr",
                "quantity": 50,
                "unit": "rim",
                "unit_price": 30000,
                "total": 1500000
            }
        ],
        "total_amount": 1500000,
        "currency": "IDR",
        "po_number": "PO-7890",
        "payment_terms": "NET 30"
    },

    # Valid Invoice 2 - IT Equipment
    {
        "invoice_number": "INV-2025-002",
        "invoice_date": "2025-07-11",
        "vendor": {
            "name": "PT. Tech Solutions",
            "code": "VEN-1002",
            "tax_id": "02.345.678.9-123.000"
        },
        "items": [
            {
                "description": "Laptop Dell",
                "quantity": 5,
                "unit": "unit",
                "unit_price": 12000000,
                "total": 60000000
            }
        ],
        "total_amount": 60000000,
        "currency": "IDR",
        "po_number": "PO-7891",
        "payment_terms": "NET 14"
    },

    # Valid Invoice 3 - Furniture
    {
        "invoice_number": "INV-2025-003",
        "invoice_date": "2025-07-12",
        "vendor": {
            "name": "PT. Furniture Indah",
            "code": "VEN-1003",
            "tax_id": "03.456.789.0-234.000"
        },
        "items": [
            {
                "description": "Meja Meeting",
                "quantity": 2,
                "unit": "unit",
                "unit_price": 3500000,
                "total": 7000000
            }
        ],
        "total_amount": 7000000,
        "currency": "IDR",
        "po_number": "PO-7892",
        "payment_terms": "NET 45"
    },

    # Valid Invoice 4 - Stationery
    {
        "invoice_number": "INV-2025-004",
        "invoice_date": "2025-07-13",
        "vendor": {
            "name": "PT. Alat Tulis",
            "code": "VEN-1004",
            "tax_id": "04.567.890.1-345.000"
        },
        "items": [
            {
                "description": "Pulpen",
                "quantity": 200,
                "unit": "pcs",
                "unit_price": 5000,
                "total": 1000000
            }
        ],
        "total_amount": 1000000,
        "currency": "IDR",
        "po_number": "PO-7893",
        "payment_terms": "NET 7"
    },

    # Valid Invoice 5 - Printing Services
    {
        "invoice_number": "INV-2025-005",
        "invoice_date": "2025-07-14",
        "vendor": {
            "name": "CV. Printing Express",
            "code": "VEN-1005",
            "tax_id": "05.678.901.2-456.000"
        },
        "items": [
            {
                "description": "Brosur A4 Full Color",
                "quantity": 5000,
                "unit": "lembar",
                "unit_price": 750,
                "total": 3750000
            }
        ],
        "total_amount": 3750000,
        "currency": "IDR",
        "po_number": "PO-7894",
        "payment_terms": "NET 14"
    },

    # Valid Invoice 6 - Networking Equipment
    {
        "invoice_number": "INV-2025-006",
        "invoice_date": "2025-07-15",
        "vendor": {
            "name": "PT. Tech Solutions",
            "code": "VEN-1002",
            "tax_id": "02.345.678.9-123.000"
        },
        "items": [
            {
                "description": "Switch 24-Port",
                "quantity": 3,
                "unit": "unit",
                "unit_price": 2500000,
                "total": 7500000
            }
        ],
        "total_amount": 7500000,
        "currency": "IDR",
        "po_number": "PO-7895",
        "payment_terms": "NET 30"
    },

    # INVALID Invoice 7 - Missing PO Number
    {
        "invoice_number": "INV-2025-007",
        "invoice_date": "2025-07-16",
        "vendor": {
            "name": "CV. Logistik Cepat",
            "code": "VEN-1006",
            "tax_id": "06.789.012.3-567.000"
        },
        "items": [
            {
                "description": "Jasa Pengiriman",
                "quantity": 1,
                "unit": "paket",
                "unit_price": 500000,
                "total": 500000
            }
        ],
        "total_amount": 500000,
        "currency": "IDR",
        "po_number": "",  
        "payment_terms": "NET 15"
    },

    # Valid Invoice 8 - Construction Materials
    {
        "invoice_number": "INV-2025-008",
        "invoice_date": "2025-07-17",
        "vendor": {
            "name": "PT. Bahan Bangunan",
            "code": "VEN-1007",
            "tax_id": "07.890.123.4-678.000"
        },
        "items": [
            {
                "description": "Semen",
                "quantity": 100,
                "unit": "sak",
                "unit_price": 75000,
                "total": 7500000
            }
        ],
        "total_amount": 7500000,
        "currency": "IDR",
        "po_number": "PO-7896",
        "payment_terms": "NET 30"
    },

    # Valid Invoice 9 - Beverages
    {
        "invoice_number": "INV-2025-009",
        "invoice_date": "2025-07-18",
        "vendor": {
            "name": "CV. Minuman Segar",
            "code": "VEN-1008",
            "tax_id": "08.901.234.5-789.000"
        },
        "items": [
            {
                "description": "Air Mineral",
                "quantity": 10,
                "unit": "karton",
                "unit_price": 40000,
                "total": 400000
            }
        ],
        "total_amount": 400000,
        "currency": "IDR",
        "po_number": "PO-7897",
        "payment_terms": "NET 14"
    },

    # INVALID Invoice 10 - Wrong Tax ID Format
    {
        "invoice_number": "INV-2025-010",
        "invoice_date": "2025-07-19",
        "vendor": {
            "name": "PT. Impor Barang",
            "code": "VEN-1009",
            "tax_id": "123456789"  
        },
        "items": [
            {
                "description": "Barang Impor",
                "quantity": 1,
                "unit": "unit",
                "unit_price": 5000000,
                "total": 5000000
            }
        ],
        "total_amount": 5000000,
        "currency": "IDR",
        "po_number": "PO-7898",
        "payment_terms": "NET 30"
    }
]