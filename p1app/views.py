from django.shortcuts import render

def work_update_create(request):
    return render(
        request,
        "p1app/work_updates/work_update_form.html"
    )
