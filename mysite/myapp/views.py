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


def workhour(request):
    if request.method =='POST':
        fd = request.POST.get('t1')
        h = workinghour(name=fd)
        h.save()
        th = workinghour.objects.all()
        return render(request, 'workinghour.html', {'th': th})

    else:
        th = workinghour.objects.all()
        return render(request, 'workinghour.html', {'th': th})

def changehrstatus(request):
    i = int(request.GET.get('hid'))
    h = workinghour.objects.get(id=i)
    s = h.status
    # print(s)
    if s==True:
        h = workinghour.objects.filter(id=i).update(status=False)
    if s==False:
        h = workinghour.objects.filter(id=i).update(status=True)
    return JsonResponse({'status':'success'})

def optortargetrep(request):
    opi = request.GET.get('oid')
    iop = int(opi)
    op_obj = operator.objects.get(id=iop)
    lie = op_obj.line
    l_obj = line.objects.get(line_name=lie)
    today = datetime.date.today()
    otr = operatortargetrep.objects.filter(operatorname=op_obj,created_date=today)
    if otr:
        return JsonResponse({'status':'error'})
    else:
        o = operatortargetrep(operatorname=op_obj,line=l_obj)
        o.save()
        # operatortargetrep id
        oprep = o.id
        oprobj = operatortargetrep.objects.get(id=oprep)
        por = opreport(operatortargetrep=oprobj)
        por.save()
        hr = workinghour.objects.filter(status=True)
        
        for h in hr:
            opr = operatortargetrep.objects.get(id=oprep)
            hrp = hourlytargetrep(optname=opr, timehr=h)
            hrp.save()
            # h+=1

        return JsonResponse({'status':'success'})
    

def update_h1(request):
    dvrtblid = request.GET.get('dvrtblid')
    a1 = request.GET.get('a1')
    rid = int(dvrtblid)
    h1 = int(a1)
    rr = daily_report.objects.filter(id=rid)
    rr.update(h1=h1)
    rg = daily_report.objects.get(id=rid)
    u1 = rg.h1
    u2 = rg.h2
    u3 = rg.h3
    u4 = rg.h4
    u5 = rg.h5
    u6 = rg.h6
    u7 = rg.h7
    u8 = rg.h8
    u9 = rg.h9
    u10 = rg.h10
    u11 = rg.h11
    u12 = rg.h12
    total = u1+u2+u3+u4+u5+u6+u7+u8+u9+u10+u11+u12
    rr.update(target_qty=total)
    return JsonResponse({'status':'success'})

def update_h2(request):
    dvrtblid = request.GET.get('dvrtblid')
    a2 = request.GET.get('a2')
    rid = int(dvrtblid)
    h2 = int(a2)
    rr = daily_report.objects.filter(id=rid)
    rr.update(h2=h2)
    rg = daily_report.objects.get(id=rid)
    u1 = rg.h1
    u2 = rg.h2
    u3 = rg.h3
    u4 = rg.h4
    u5 = rg.h5
    u6 = rg.h6
    u7 = rg.h7
    u8 = rg.h8
    u9 = rg.h9
    u10 = rg.h10
    u11 = rg.h11
    u12 = rg.h12
    total = u1+u2+u3+u4+u5+u6+u7+u8+u9+u10+u11+u12
    rr.update(target_qty=total)
    return JsonResponse({'status':'success'})

def update_h3(request):
    dvrtblid = request.GET.get('dvrtblid')
    a3 = request.GET.get('a3')
    rid = int(dvrtblid)
    h3 = int(a3)
    rr = daily_report.objects.filter(id=rid)
    rr.update(h3=h3)
    rg = daily_report.objects.get(id=rid)
    u1 = rg.h1
    u2 = rg.h2
    u3 = rg.h3
    u4 = rg.h4
    u5 = rg.h5
    u6 = rg.h6
    u7 = rg.h7
    u8 = rg.h8
    u9 = rg.h9
    u10 = rg.h10
    u11 = rg.h11
    u12 = rg.h12
    total = u1+u2+u3+u4+u5+u6+u7+u8+u9+u10+u11+u12
    rr.update(target_qty=total)
    return JsonResponse({'status':'success'})


#Have Error            
def hourlydata(request):
    op = operatortargetrep.objects.all()
    htr = hourlytargetrep.objects.all()
    opo = opreport.objects.all()
    hr = workinghour.objects.filter(status=True)

    oplist = list(op)

    print(type(oplist))
    context = {'op':op, 'htr':htr, 'hr':hr, 'opo':opo}
    return render(request, 'hourlydata.html',context)




    
