#i created this. BibashJr
from django.http import HttpResponse
from django.shortcuts import render
from googletrans import Translator


def index(request):
  
    return  render(request, 'index.html')

def about(request):
    return HttpResponse("know about")

def ex1(request):
    s="<h1> nav bar</h1>"
    return HttpResponse(s)

def analyze(request):
     djtext = request.GET.get('text', 'default')
     removepunc = request.GET.get('removepunc', 'off')
     translatejp = request.GET.get('translatejp', 'off')
     
     if removepunc == "on" :
            punctuations = '''!(){}[],:;,.()_+-=.<>/?'''
            analyzed = ""
            for char in djtext:
             if char not in punctuations:
                analyzed = analyzed + char
            params = {'purpose': 'removed punctation', 'Analyzed_text': analyzed}
            return render(request, 'analyze.html', params)
    
   
     elif translatejp == "on":
        translated_text = translate_english_to_japanese(djtext)
        if translated_text is not None:
            params = {'purpose': 'English to Japanese translation', 'Analyzed_text': translated_text}
            return render(request, 'analyze.html', params)
        else:
            return HttpResponse("Translation failed")

     else:
         return HttpResponse("Error")


def translate_english_to_japanese(text):
    translator = Translator(service_urls=['translate.google.com', 'translate.google.co.kr'])
    translated = translator.translate(text, src='en', dest='ja').text()
    return translated