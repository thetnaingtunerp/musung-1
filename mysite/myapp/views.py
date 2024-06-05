from django.shortcuts import render,redirect,HttpResponse
from django.http import JsonResponse
from django.shortcuts import (get_object_or_404,
                            render,
                            HttpResponseRedirect)
import datetime
# today = datetime.date.today()
from .models import *
from .forms import *

def operatorlist(request):
    op = operator.objects.all()
    form = OptForm()
    context = {'op':op, 'form':form}
    return render(request, 'operatorlist.html', context)

def save_operator(request):
    if request.method == 'POST':
        form = OptForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('myapp:operatorlist')
    else:
        return redirect('myapp:operatorlist')
    return redirect('myapp:operatorlist')


def linelist(request):
    lis = line.objects.all()
    context = {'lis':lis}
    return render(request, 'line.html', context)

def update_line_target(request):
    lid = request.GET.get('lid')
    ltarget = request.GET.get('ltarget')
    
    # change int type
    i = int(lid)
    t = int(ltarget)
    l = line.objects.filter(id=i).update(target=t)
    return JsonResponse({'status':'success'})

def operatortarget(request,id):
    lis = line.objects.all()
    op = daily_report.objects.filter(line=id)
    context = {'lis':lis, 'op':op}
    return render(request, 'operatortarget.html', context)

def operatoratt(request,id):
    op = operator.objects.filter(line=id)
    context = {'op':op}
    return render(request, 'operatoratt.html', context)

def save_att_daily(request):
    opi = request.GET.get('oid')
    iop = int(opi)
    op_obj = operator.objects.get(id=iop)
    lie = op_obj.line
    l_obj = line.objects.get(line_name=lie)
    # print(l_obj)
    dr = daily_report(operator_name=op_obj, line=l_obj)
    dr.save()
    return JsonResponse({'status':'success'})

def daily_rep_view(request):
    today = datetime.date.today()
    lis = line.objects.all()
    op = daily_report.objects.filter(created_date=today)
    context = {'lis':lis, 'op':op}
    return render(request, 'daily_rep_view.html', context)

def save_daily_rep_view(request):
    ot1 = int(request.GET.get('ot1'))
    ot2 = int(request.GET.get('ot2'))
    ot3 = int(request.GET.get('ot3'))
    ot4 = int(request.GET.get('ot4'))
    ot5 = int(request.GET.get('ot5'))
    ot6 = int(request.GET.get('ot6'))
    ot7 = int(request.GET.get('ot7'))
    ot8 = int(request.GET.get('ot8'))
    ot9 = int(request.GET.get('ot9'))
    ot10 = int(request.GET.get('ot10'))
    ot11 = int(request.GET.get('ot11'))
    dvrtblid = int(request.GET.get('dvrtblid'))

    total = ot1+ot2+ot3+ot4+ot5+ot6+ot7+ot8+ot9+ot10+ot11

    r = daily_report.objects.filter(id=dvrtblid)
    ab = daily_report.objects.get(id=dvrtblid)
    a = ab.line
    l = line.objects.filter(line_name=a)
    lt = l[0].target
    # print(type(lt))
    percen = (total/lt)*100
    # print(percen)
    r.update(h1=ot1,h2=ot2, h3=ot3, h4=ot4, h5=ot5, h6=ot6, h7=ot7, h8=ot8, h9=ot9, h10=ot10, h11=ot11, target_qty=total, target_per=percen)

    return JsonResponse({'status':'success'})


def daily_rep_filter_by_line(request,id):
    today = datetime.date.today()
    lis = line.objects.all()
    ls = line.objects.get(id=id)
    op = daily_report.objects.filter(created_date=today,line=ls)
    context = {'lis':lis, 'op':op}
    return render(request, 'daily_rep_view.html', context)

def daily_rep_filter_operator(request,id):
    # gop = request.GET.get('id')
    p =  operator.objects.get(id=id)
    pk = id
    op = daily_report.objects.filter(operator_name=p)
    context = {'op':op, 'optr_obj':pk}
    return render(request, 'daily_rep_filter_operator.html', context)

def daily_rep_filter_bydate(request):
    if request.method == 'POST':
        fd = request.POST.get('fdate')
        ed = request.POST.get('edate')
        oj = request.POST.get('oj')

        p = operator.objects.get(id=oj)
        opr = daily_report.objects.filter(created_date__range=[fd, ed],operator_name=p)

        context = {'op':opr}
        return render(request, 'daily_rep_filter_bydate.html', context)
    else:
        return HttpResponse('error')
    
def monthly_report(request):
    if request.method=="POST":
        fd = request.POST.get('fdate')
        ed = request.POST.get('edate')
        opr = daily_report.objects.filter(created_date__range=[fd, ed])
        context = {'op':opr,}
        return render(request, 'monthly_report.html', context)
    else:
        opr = daily_report.objects.all()
        context = {'op':opr,}
        return render(request, 'monthly_report.html', context)


def testfor(request):
    if request.method =='POST':
        fd = request.POST.get('t1')
        h = workinghour(name=fd)
        h.save()
        th = workinghour.objects.all()
        return render(request, 'test/test.html', {'th': th})

    else:
        th = workinghour.objects.all()
        return render(request, 'test/test.html', {'th': th})


    
