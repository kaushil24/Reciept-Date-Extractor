import textExt as te
from PIL import Image
import re
import dateparser

# op = tx.extractTxt(tx, "1ae93f0a.jpeg")
# op = extr.extractTxt("")

class dateExtractor():

    def formatMaker(self, date, month, year):
        if int(month)>12:
            date, month = month, date
        
        if len(date)==1:
            date = '0'+date
        if len(month)==1:
            month = '0'+month
        if len(year)==2:
            year="20"+year
       
        return year+"-"+month+"-"+date


    def extractDate(self, content):
        
        self.date = ''
        self.mnths = ["jan", "jeb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]

        # For Dates like: 6.12.2019 or 06-2-2019 or 06/12/2019 etc
        if re.search(r"\d{1,2}[./-]\d{1,2}[.-/]\d{2,4}", content):
            temp = re.findall(r"\d{1,2}[./-]\d{1,2}[.-/]\d{2,4}", content)[0]
            ls = re.split(r"[./-]", temp)
            return self.formatMaker(ls[0], ls[1], ls[2])

 

        # For dates like: 24.Jun.19 or 2.Jan.2019
        elif re.search(r"\d{1,2}[/.-][a-z]{3}[./-]\d{2,4}", content.lower()):
            temp = re.findall(r"\d{1,2}[/.-][a-z]{3}[./-]\d{2,4}", content.lower())[0]
            ls = re.split("[./-]", temp)
            return self.formatMaker(ls[0], str(self.mnths.index(ls[1])+1), ls[2])
            
        # For dates like: Apr07'19
        elif re.search(r"[a-z]{3}\d{1,2}\'\d{2,4}", content.lower()):
            content = content.lower()
            temp = re.findall(r"[a-z]{3}\d{1,2}\'\d{2,4}", content)[0]
            
            d = re.sub(r"^[a-z]", "", temp[-5:-3])
            m = str(self.mnths.index(temp[:3])+1)
            y = temp[-2:]
            
            return self.formatMaker(d, m, y)


        else:
            return "NaN"


if __name__ == "__main__":


    # f = open("./Scripts/sampleText.txt", "r")
    # st = f.read()
    textext = te.TesseractTxtExtractor()
    st = textext.extractTxt("ed731156.jpeg")
    print(st)
    dx = dateExtractor()
    date = dx.extractDate(st) 
    print(date)   