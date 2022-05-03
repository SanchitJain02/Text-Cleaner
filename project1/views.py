from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # return HttpResponse('''<h1>Hello World</h1> <a href="https://mail.google.com/mail/u/0/#inbox"> Go to Gmail</a>''')
    return render(request, "index.html")

def analyze(request):
    djtext = request.GET.get('text','default')
    removepunc = request.GET.get('removepunc','off')
    fullcapitalize = request.GET.get('fullcapitalize','off')
    newlineremover = request.GET.get('newlineremover','off')
    #analyzed = djtext
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    analyzed = ""
    if removepunc == "on":
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed punctions','analyzed_text':analyzed}
        return render(request,"analyze.html",params)
    elif(fullcapitalize == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose':'Changed to Upper case','analyzed_text':analyzed}
        return render(request,"analyze.html",params)
    elif(newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n":
                analyzed = analyzed + char
        params = {'purpose':'Removed New LineS','analyzed_text':analyzed}
        return render(request,"analyze.html",params)
    else:
        return HttpResponse(djtext)       