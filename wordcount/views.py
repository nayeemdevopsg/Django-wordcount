from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request, 'home.html')

def count(request):
    
    wordcount = request.GET['fulltext']

    countfile = wordcount.split()

    worddictionary = {}     
 
    for word in countfile:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1        

    return render(request, 'count.html', {"count1": len(countfile), "worddictionary": worddictionary.items()})


def about(request):
    return render(request, 'about.html')