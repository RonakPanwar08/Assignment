from django.urls import path
from .views import ProcessDataReceiver, ProcessDataViewer
from .views import frontend_view

urlpatterns = [
    path('process-data/', ProcessDataReceiver.as_view()),
    path('view-processes/', ProcessDataViewer.as_view()),
]
urlpatterns += [path('', frontend_view)]