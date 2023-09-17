from django.urls import path

from . import views

urlpatterns = [
    path("", views.PDFView.as_view(), name="pdf"),
    path("file/", views.PDFFileView.as_view(), name="pdf_file"),
]
