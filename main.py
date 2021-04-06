import pyttsx3
import pdfplumber

pdf = pdfplumber.open('file.pdf')

first_page = pdf.pages[1]

text = first_page.extract_text()
text = text.replace('\n', " ")

print(text)

speak = pyttsx3.init()
speak.say(text)
speak.runAndWait()