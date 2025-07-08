' Menerima argumen PERTAMA dari UiPath
poNumber = WScript.Arguments(0)

' Menyiapkan Regular Expression
Dim regEx
Set regEx = New RegExp
regEx.Pattern = "^PO-\d{4}$" 
regEx.IgnoreCase = True

' Menyiapkan objek untuk menulis file
Dim fso, resultFile
Set fso = CreateObject("Scripting.FileSystemObject")
' Membuat file result.txt di folder yang sama dengan skrip
Set resultFile = fso.CreateTextFile("result.txt", True)

' Melakukan validasi dan MENULIS hasilnya ke file teks
If regEx.Test(poNumber) Then
    resultFile.WriteLine("true")
Else
    resultFile.WriteLine("false")
End If

' Menutup file
resultFile.Close