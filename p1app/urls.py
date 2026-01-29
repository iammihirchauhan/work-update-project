from django.urls import path
from .views import work_update_create

app_name = "p1app"

urlpatterns = [
    path("new/", work_update_create, name="work-update-create"),
]
