import googletrans
from googletrans import Translator

print(googletrans.LANGUAGES)
i = 1
while i !=0 :
    i = i+1
    sentence = str(input("Çeviri -->"))
    translator = Translator(service_urls=['translate.googleapis.com'])
    translated = translator.translate(sentence, dest='en')
    print(translated)




