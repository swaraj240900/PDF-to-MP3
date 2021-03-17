import PyPDF2
from gtts import gTTS


pdfFileObj = open("Trail PDF.pdf", "rb")
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

mytext = ""

for pageNum in range(pdfReader.numPages):
    pageObj = pdfReader.getPage(pageNum)

    mytext += pageObj.extractText()
print(mytext)
pdfFileObj.close()

tts = gTTS(text=mytext, lang='en')
tts.save("Trial Audio.mp3")
