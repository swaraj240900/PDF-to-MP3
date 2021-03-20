# The PDF file should be in the same directory as the code.

import PyPDF2
from gtts import gTTS


pdfFileObj = open("xyz.pdf", "rb")    # The file name goes here
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

mytext = ""

for pageNum in range(pdfReader.numPages):
    pageObj = pdfReader.getPage(pageNum)

    mytext += pageObj.extractText()
print(mytext)
pdfFileObj.close()

tts = gTTS(text=mytext, lang='en')
tts.save("zyx.mp3")                 # The name of the MP3 file you want will go here....
