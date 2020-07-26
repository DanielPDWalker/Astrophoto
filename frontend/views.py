from django.shortcuts import render, get_object_or_404

from messier_objects.models import MessierObject


def index(request):
    return render(request, 'index.html')


def mes_obj_overview(request):
    list_of_mes_obj = MessierObject.objects.all()

    context = {
        "list_of_mes_obj": list_of_mes_obj
    }

    return render(request, 'api_frontends/messier_objects_overview.html', context)


def mes_obj_detail(request, mes_num):
    mes_obj = get_object_or_404(MessierObject, messier_number=mes_num)

    context = {
        "mes_obj": mes_obj
    }
    
    return render(request, 'api_frontends/messier_object_detail.html', context)