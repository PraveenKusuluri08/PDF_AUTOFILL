import os
class Utils:
    def __init__(self,fileName):
        self.fileName = fileName
        
    def _file_pdf(self):    
        extension = os.path.splitext(self.fileName)[-1].lower()
        if extension != ".pdf":
            raise Exception("PDF file is not valid")          
        