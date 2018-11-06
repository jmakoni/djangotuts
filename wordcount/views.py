from django.http import HttpResponse
from django.shortcuts import render
import operator
def homepage(request):
    return render(request, 'home.html', {'ki':'tewali'})

def count(request):
    fulltext = request.GET['fulltext']
    words = fulltext.split()
    wordlist = {}
    for word in words:
        if word not in wordlist:
            wordlist[word] = 1
        else:
            wordlist[word] += 1

    sortedlist = sorted(wordlist.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html',{'fulltext':fulltext,'wordcount':len(words),'sortedlist':sortedlist})

def about(request):
    return render(request, 'about.html')
