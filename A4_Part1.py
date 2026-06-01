import openpyxl
from docxtpl import DocxTemplate
from datetime import datetime
 
location = "Assignment 04.xlsx"

dataFile = openpyxl.load_workbook (location)

dataSheet = dataFile.active

dataItems = list(dataSheet.values)



myDoc = DocxTemplate(r"D:\Nam_Python\asm4\Certificate.docx")

for item in dataItems[1:]:
    date_issued = item[5]  
    if isinstance(date_issued, datetime):
        date_issued = date_issued.strftime('%B %d, %Y')
    myDoc.render({ "StudentNumber": item[0],"Name": item[1], "Grade": item[3],"SupervisorName": item[4],"UniversityName": item[2], "DateIssued":date_issued
}) 
    myDoc.save("Letter" + str(item[0]) + ".docx")
