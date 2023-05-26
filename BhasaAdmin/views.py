#i created this. BibashJr
from django.http import HttpResponse
from django.shortcuts import render
from googletrans import Translator
import pyttsx3



def index(request):
    if request.method == 'POST':
        return render(request, 'index.html')
    else:
        # Clear the analyzed text
        params = {'Analyzed_text': None, 'purpose': None, 'Pronunciation': None}
        return render(request, 'index.html', params)


def about(request):
    return HttpResponse("know about")

def ex1(request):
    s="<h1> nav bar</h1>"
    return HttpResponse(s)

def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    translatejp = request.POST.get('translatejp', 'off')
     
    if removepunc == "on" :
            punctuations = '''!(){}[],:;,.()_+-=.<>/?'''
            analyzed = ""
            for char in djtext:
             if char not in punctuations:
                analyzed += char
            params = {'purpose': 'removed punctation', 'Analyzed_text': analyzed}
         
            djtext = analyzed

    if translatejp == "on":
        translated_text, pronunciation = translate_english_to_japanese(djtext)
        if translated_text is not None:
            params = {'purpose': 'English to Japanese translation', 'Analyzed_text': translated_text, }
            if pronunciation is not None:
                params['Pronunciation'] = pronunciation
                generate_speech(pronunciation)
                
          
                return render(request,'index.html', params)
           
            else:
             return HttpResponse("Translation failed")
        else:
          return HttpResponse("Error")
        
def translate_english_to_japanese(text):
    translator = Translator(service_urls=['translate.google.com', 'translate.google.co.kr' ])
    translated = translator.translate(text, src='en', dest='ja')
    pronunciation = translated.pronunciation

    return translated.text, translated.pronunciation

def generate_speech(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 125) 
     # Set the speech rate (words per minute)
    engine.setProperty('volume', 0.8)  # Adjust the volume (optional)

    engine.say(text)
    engine.runAndWait()

    return engine.getProperty('voice')
