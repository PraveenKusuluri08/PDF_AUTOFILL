import PyPDF2

pdf_reader = PyPDF2.PdfReader("g-28.pdf")

writer = PyPDF2.PdfWriter()


page = pdf_reader.pages[1]

fields1 = pdf_reader.get_fields()

writer.add_page(page)
fields =pdf_reader.get_form_text_fields()

# print(fields)

print(fields1)

# print(pdf_reader.get_fields())     
# writer.update_page_form_field_values(
#     writer.pages[0],{"Line9_DaytimeTelephoneNumber[0]":"1234567890"}
# )

# with open("g-28.pdf","wb") as ot:
#     writer.write(ot)
    