import os
from django.http import FileResponse
from django.views import View
from django.views.generic import TemplateView


class PDFView(TemplateView):
    template_name = "pdf/pdf.html"


class PDFFileView(View):
    def get(self, request):
        return FileResponse(
            open(os.path.join(os.path.dirname(__file__), "sample.pdf"), "rb")
        )
