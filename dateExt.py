import textExt as te
from PIL import Image
import re
import dateparser
from autocorrect import Speller

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
        self.mnths = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
        self.months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']

        
        # To check for Jan 8, 2019 etc..
        contentSet = set(content.lower().split()) #.replace("'", ' ').replace(",", " ").replace(""))
        mnthsSet = set(self.mnths)
        common = contentSet & mnthsSet
        common1 = contentSet & set(self.months)  

        if common:
            print(common)
            x = ''.join(common)
            idx = content.lower().split().index(x)
            mnt = str(self.mnths.index(x) + 1)
            date = content.lower().split()[idx+1].replace(",", '').replace("-", '').replace("'", '')
            if idx+5 > len(content.lower().split()):
                temp_year = ''.join(content.lower().split()[idx+2])
            else:
                temp_year = ''.join(content.lower().split()[idx+2:idx+5])
            year = re.findall(r"\d{2,4}", temp_year)[0]
            return self.formatMaker(date, mnt, year)

        elif common1:
            print(common1)
            x = ''.join(common1)
            idx = content.lower().split().index(x)
            mnt = str(self.months.index(x) + 1)
            date = content.lower().split()[idx+1].replace(",", '').replace("-", '').replace("'", '')
            if idx+5 > len(content.lower().split()):
                temp_year = ''.join(content.lower().split()[idx+2])
            else:
                temp_year = ''.join(content.lower().split()[idx+2:idx+5])
            year = re.findall(r"\d{2,4}", temp_year)[0]
            return self.formatMaker(date, mnt, year)

        
        
        # For Dates like: 6.12.2019 or 06-2-2019 etc
        if re.search(r"\d{1,2}[.-]\d{1,2}[.-]\d{2,4}", content):
            temp = re.findall(r"\d{1,2}[.-]\d{1,2}[.-]\d{2,4}", content)[0]
            ls = re.split(r"[./-]", temp)
            return self.formatMaker(ls[0], ls[1], ls[2])

        # For dates like: 6/12/2019 or 06/02/19
        elif re.search(r"\d{1,2}[/]\d{1,2}[/]\d{2,4}", content):
            temp = re.findall(r"\d{1,2}[/]\d{1,2}[/]\d{2,4}", content)[0]
            ls = re.split(r"[./-]", temp)
            return self.formatMaker(ls[0], ls[1], ls[2])

        # For dates like: 24.Jun.19 or 2/Jan/2019 
        elif re.search(r"\d{1,2}[/.-][a-z]{3}[./-]\d{2,4}", content.lower()):
            temp = re.findall(r"\d{1,2}[/.-][a-z]{3}[./-]\d{2,4}", content.lower())[0]
            ls = re.split("[./-]", temp)
            return self.formatMaker(ls[0], str(self.mnths.index(ls[1])+1), ls[2])
  
            
        # For dates like: 'jan 28, 2019', 'december 29, 2018', 'jul 1, 2019', "sep07'18", "apr07'16"
        elif re.search(r"[a-z]{3,9}[\s]*\d{1,2}[\s',]+\d{2,4}", content.lower()): # Alternate string : r"[a-z]{3,9}[\s']*\d{1,2}[\s.',]+\d{2,4}"
            content = content.lower()
            temp = re.findall(r"[a-z]{3,9}[\s']*\d{1,2}[\s',]+\d{2,4}", content)[0]
            print("********", temp, "****************")
            # d = re.sub(r"^[a-z]", "", temp[-5:-3])
            # m = str(self.mnths.index(temp[:3])+1)
            # y = temp[-2:]
            speller = Speller(lang="en")
            temp = speller(temp)
            m = re.findall(r"^[a-z]{3}", temp)[0]
            print(m)

            d = list(map((lambda x: x[1:-1]), re.findall(r"[\D]\d{1,2}[\D]", temp)))[0]
            if m not in self.mnths:
                return "NaN"
            else:
                m = self.mnths.index(m)+1
                y = temp[-2:] 
                return self.formatMaker(d, str(m), y)

          
           # d = re.find("\s\d{1,2}")

        else:
            return "NaN"


if __name__ == "__main__":


    # f = open("./Scripts/sampleText.txt", "r")
    # st = f.read()
    textext = te.TesseractTxtExtractor()
    st = textext.extractTxt(imgNme="02acce30.jpeg")
    print(st)
    dx = dateExtractor()
    date = dx.extractDate(st) 
    print(date)   