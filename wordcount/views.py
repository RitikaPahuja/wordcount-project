from django.http import HttpResponse
from django.shortcuts import render
import operator
def home(request):
    return render(request,'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordlen = fulltext.split()
    worddict = {}
    for word in wordlen:
        if word in worddict:
            worddict[word] += 1

        else:
            worddict[word] = 1
    li = sorted(worddict.items(),key=operator.itemgetter(1),reverse=True)
    return render(request,'count.html',{'fulltext':fulltext,'count':len(wordlen),'sortedwords':li})

def about(request):
    return render(request,'about.html')
