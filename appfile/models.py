from django.db import models
# import PyPDF2
# import re

class Quote(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=100)
    source = models.CharField(max_length=200, blank=True)
    # file = models.FileField(upload_to='quotes/', default='default.pdf')
    # def extract_from_pdf(self):
    #    with open(self.file.path, 'rb') as file:
          
    #         pdf = PyPDF2.PdfFileReader(file)
    #         for page in range(pdf.getNumPages()):
    #             text = pdf.getPage(page).extractText()
    #             lines = text.split('\n')
    #             for line in lines:
    #                     match = re.search(r'"(.*?)"\s*-\s*(.*)', line)
    #                     if match:
    #                      quote_text = match.group(1)
    #                      author = match.group(2)
    #                      elf.text = quote_text
    #                      self.author = author
    #                      self.save()      


class Admin(models.Model):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('regular', 'Regular user'),
    )
    username = models.CharField(max_length=30, unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='regular')

    def can_add_quote(self):
        return self.role == 'admin'


                


    

             

    
               







