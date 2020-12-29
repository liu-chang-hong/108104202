from django.shortcuts import render, redirect
from django.http import HttpResponse
from mainsite.models import PlayList, Video, Post
from mainsite.models import AccessInfo, Branch, StoreIncome ,Data
import random
from datetime import datetime

def homepage(request):
    rec = AccessInfo()
    rec.save()
    hit_count = len(AccessInfo.objects.all())
    posts = Post.objects.all()
    now = datetime.now()
    return render(request,"index.html", locals())

def mychart(request, bid=0):
    rec = AccessInfo()
    rec.save()
    hit_count = len(AccessInfo.objects.all())
    now = datetime.now()
    branches = Branch.objects.all()
    if bid == 0:
        data = StoreIncome.objects.all()
    else:
        data = StoreIncome.objects.filter(branch=bid)
    return render(request, "mychart.html", locals())

def chart(request, year=0, month=0):
    rec = AccessInfo()
    rec.save()
    hit_count = len(AccessInfo.objects.all())
    now = datetime.now()
    branches = Branch.objects.all()
    if year == 0:
        data = StoreIncome.objects.all()
    else:
        data = StoreIncome.objects.filter(income_year=year)
        if month>0:
            data = data.filter(income_month=month)
    if year>0 and month>0:
        title ="{}年{}月各分店營收情形".format(year, month)
    elif year>0:
        title ="{}年".format(year)
    else:
        title = "各分店營收情形"
    return render(request, "mychart.html", locals())
def lotto(request):
    rec = AccessInfo()
    rec.save()
    hit_count = len(AccessInfo.objects.all())
    now = datetime.now()
    lucky_no = random.randint(1, 42)
    numbers = list()
    for i in range(6):
        numbers.append(random.randint(1, 42))

    return render(request,"lotto.html", locals())

def playlist(request):
    rec = AccessInfo()
    rec.save()
    hit_count = len(AccessInfo.objects.all())
    now = datetime.now()
    items = PlayList.objects.all()
    return render(request, "playlist.html", locals())

def showlist(request, id):
    rec = AccessInfo()
    rec.save()
    hit_count = len(AccessInfo.objects.all())
    now = datetime.now()
    titles = Video.objects.filter(plist=id)
    return render(request, "showlist.html", locals())
    
def showpost(request, slug):
    rec = AccessInfo()
    rec.save()
    hit_count = len(AccessInfo.objects.all())
    now = datetime.now()
    try:
        post = Post.objects.get(slug = slug)
        if post != None:
            return render(request, "post.html", locals())
    except:
        return redirect("/")

def temperture(request):
    rec = AccessInfo()
    rec.save()
    hit_count = len(AccessInfo.objects.all())
    now = datetime.now()
    data = Data.objects.all()
    return render(request, "temperture.html", locals())

def temperture1(request):
    rec = AccessInfo()
    rec.save()
    hit_count = len(AccessInfo.objects.all())
    now = datetime.now()
    return render(request, "temperture1.html", locals())

def temperture2(request):
    rec = AccessInfo()
    rec.save()
    hit_count = len(AccessInfo.objects.all())
    now = datetime.now()
    return render(request, "temperture2.html", locals())

def temperture3(request):
    rec = AccessInfo()
    rec.save()
    hit_count = len(AccessInfo.objects.all())
    now = datetime.now()
    return render(request, "temperture3.html", locals())

def temperture4(request):
    rec = AccessInfo()
    rec.save()
    hit_count = len(AccessInfo.objects.all())
    now = datetime.now()
    return render(request, "temperture4.html", locals())

def temperture5(request):
    rec = AccessInfo()
    rec.save()
    hit_count = len(AccessInfo.objects.all())
    now = datetime.now()
    return render(request, "temperture5.html", locals())

def temperture6(request):
    rec = AccessInfo()
    rec.save()
    hit_count = len(AccessInfo.objects.all())
    now = datetime.now()
    return render(request, "temperture6.html", locals())

def temperture7(request):
    rec = AccessInfo()
    rec.save()
    hit_count = len(AccessInfo.objects.all())
    now = datetime.now()
    return render(request, "temperture7.html", locals())

def temperture8(request):
    rec = AccessInfo()
    rec.save()
    hit_count = len(AccessInfo.objects.all())
    now = datetime.now()
    return render(request, "temperture8.html", locals())

def temperture9(request):
    rec = AccessInfo()
    rec.save()
    hit_count = len(AccessInfo.objects.all())
    now = datetime.now()
    return render(request, "temperture9.html", locals())

def temperture10(request):
    rec = AccessInfo()
    rec.save()
    hit_count = len(AccessInfo.objects.all())
    now = datetime.now()
    return render(request, "temperture10.html", locals())

def temperture11(request):
    rec = AccessInfo()
    rec.save()
    hit_count = len(AccessInfo.objects.all())
    now = datetime.now()
    return render(request, "temperture11.html", locals())

def temperture12(request):
    rec = AccessInfo()
    rec.save()
    hit_count = len(AccessInfo.objects.all())
    now = datetime.now()
    return render(request, "temperture12.html", locals())

def temperture13(request):
    rec = AccessInfo()
    rec.save()
    hit_count = len(AccessInfo.objects.all())
    now = datetime.now()
    return render(request, "temperture13.html", locals())    

def temperture14(request):
    rec = AccessInfo()
    rec.save()
    hit_count = len(AccessInfo.objects.all())
    now = datetime.now()
    return render(request, "temperture14.html", locals())

def temperture15(request):
    rec = AccessInfo()
    rec.save()
    hit_count = len(AccessInfo.objects.all())
    now = datetime.now()
    return render(request, "temperture15.html", locals())

def temperture16(request):
    rec = AccessInfo()
    rec.save()
    hit_count = len(AccessInfo.objects.all())
    now = datetime.now()
    return render(request, "temperture16.html", locals())

def temperture17(request):
    rec = AccessInfo()
    rec.save()
    hit_count = len(AccessInfo.objects.all())
    now = datetime.now()
    return render(request, "temperture17.html", locals())

def temperture18(request):
    rec = AccessInfo()
    rec.save()
    hit_count = len(AccessInfo.objects.all())
    now = datetime.now()
    return render(request, "temperture18.html", locals())

def temperture19(request):
    rec = AccessInfo()
    rec.save()
    hit_count = len(AccessInfo.objects.all())
    now = datetime.now()
    return render(request, "temperture19.html", locals())