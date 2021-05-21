from django.shortcuts import render
from django.views.generic import DetailView, View

def GroupListView(request):
    return render(request,
            "group/group_list.html"
        )


class GroupDetail(View):
    """
    그룹 디테일
    """
    pass