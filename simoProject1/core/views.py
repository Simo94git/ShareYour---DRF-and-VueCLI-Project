from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView #renderizza dei template

#per produzione dopo npm run build
from django.conf import settings


# questa view ci permette ci richiamare un template
#attraverso un pattern url
#
class IndexTemplateView(LoginRequiredMixin, TemplateView):
	def get_template_names(self):  #è un metodo sovrascritto da TemplateView
		if settings.DEBUG:
			template_name = "index-development.html"
		else:
			template_name = "index.html"

		return template_name