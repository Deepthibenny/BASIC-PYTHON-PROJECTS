import  pyttsx3
book=open(r"C:\Users\debenny\Downloads\AudioBook Program\Customer.txt")
book_text=book.readlines()
engine=pyttsx3.init()
for i in book_text:
    engine.say(i)
    engine.runAndWait()
