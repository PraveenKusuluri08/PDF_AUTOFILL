import PyPDF2
from json import dumps
from flask import jsonify, request


class PDFController:
    def __init__(self, fileName):
        self.file = fileName

    def _get_fields(self) -> any:
        
        print("self.file",self.file)
        file_reader = PyPDF2.PdfReader(self.file)

        form_Data = file_reader.get_fields()

        data = {}

        for k, v in form_Data.items():
            data[k] = {
                'value': v.get("/V"),
                'type': v.get("/FT"),
                "name": v.get("/T")
            }
        return jsonify(data)

    def _update_pdf(self, data) -> dumps:
        writer = PyPDF2.PdfWriter()
        file_reader = PyPDF2.PdfReader(self.file)
        page = file_reader.pages[1]
        field = data.keys()
        fieldName = [*field][0]
        value = data.values()

        for page_num in range(len(file_reader.pages)):
            page = file_reader.pages[page_num]

            fields = file_reader.get_fields()
            writer.add_page(page)

            for field in fields:
                f = fields[field]
                if field == fieldName and f["/FT"] == '/Btn':
                    print("🥊", f)

                    writer.update_page_form_field_values(
                        writer.pages[page_num], {fieldName: '/Y'}
                    )
                if field == fieldName and f["/FT"] == '/Ch':
                    print("🛼", f)
                    writer.update_page_form_field_values(
                        writer.pages[page_num], {fieldName: "NY"}
                    )
                if field in fieldName and f["/FT"] == '/Tx':
                    writer.update_page_form_field_values(
                        writer.pages[page_num], {f["/T"]: [*value][0]}
                    )

        outPutPdf = open("output.pdf", "wb")
        writer.write(outPutPdf)
        outPutPdf.close()

        return jsonify({"message": f"field {fieldName} is updated successfully"})

    def _update_fields(self, data):
        file_reader = PyPDF2.PdfReader(self.file)
        writer = PyPDF2.PdfWriter()

        fieldKeys = []
        [fieldKeys.extend(obj.keys()) for obj in data]
        fieldValues = []
        [fieldValues.extend(obj.values()) for obj in data]
        print(fieldKeys)

        for page_num in range(len(file_reader.pages)):
            page = file_reader.pages[page_num]

            fields = file_reader.get_fields()
            writer.add_page(page)
            for field in fields:
                for k in range(len(fieldKeys)):
                    f = fields[fieldKeys[k]]
                    print("🙂", f)
                    if field == fieldKeys[k] and f["/FT"] == '/Btn':

                        writer.update_page_form_field_values(
                            writer.pages[page_num], {fieldKeys[k]: '/N'}
                        )

                    if field == fieldKeys[k] and f["/FT"] == '/Ch':
                        writer.update_page_form_field_values(
                            writer.pages[page_num], {fieldKeys[k]: "NY"}
                        )

                    if field in fieldKeys[k] and f["/FT"] == '/Tx':
                        writer.update_page_form_field_values(
                            writer.pages[page_num], {f["/T"]: fieldValues[k]}
                        )
                        
                    if field == fieldKeys[k]:
                        writer.update_page_form_field_values(
                            writer.pages[page_num], {
                                fieldKeys[k]: fieldValues[k]}
                        )

        with open("output.pdf", "wb") as ot:
            writer.write(ot)
            ot.close()
        return jsonify({"message":"Fields specified are updated successfully"})
    
    