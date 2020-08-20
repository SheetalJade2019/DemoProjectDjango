from django.shortcuts import render

# Create your views here.

def index(request):
    ct = request.session.get('count',0)
    new_cnt = ct + 1
    request.session['count'] = new_cnt
    return render(request,'AppPageCount/index.html',{'c':new_cnt})
