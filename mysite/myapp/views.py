from django.shortcuts import render,redirect,HttpResponse
from django.http import JsonResponse
from django.shortcuts import (get_object_or_404,
                            render,
                            HttpResponseRedirect)


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