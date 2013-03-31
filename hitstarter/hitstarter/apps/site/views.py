# top-level views for the project, which don't belong in any specific app

from django.views.generic.base import TemplateView


class HomePage(TemplateView):

    template_name = "index.html"
