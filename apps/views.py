from django.shortcuts import get_object_or_404, render, redirect, reverse
# from django.views.generic import DetailView, View
from django.db import models
from apps import models as apps_models
from django.template import loader
from django.http import HttpResponse


def IndexView(request):
    return render(request, "index.html")

def ClassListView(request):
    return render(request,
            "group/group_list.html"
        )

def class_detail(request, class_id):
    classs = get_object_or_404(apps_models.Class, pk=class_id)
    # classs = apps_models.Class.object.get(pk = class_id)
    context = {'class':classs}

    return render(request, 'group/group_detail.html', context)

# class ClassDetail(DetailView):
#     """ Group Detail Definition """

#     model = models.Class
#     template_name = "group/group_detail.html"

    # def get_context_data(self, **kwargs):
    #     context = super(ClassDetail, self).get_context_data(**kwargs)
    #     context['payments'] = Invoice.objects.filter(classs=self.object)
    #     return context