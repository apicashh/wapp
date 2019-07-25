from django.shortcuts import render
from django.views.generic.list import ListView
from wapp.models import Gallerys, Best_sites, FHG_models
from django.views import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

class PagView(ListView):	
	def get(self, request):
		dump_list = Gallerys.objects.all().order_by("?")
		paginator = Paginator(dump_list, 42) # Show 42 contacts per page
		page = request.GET.get('page')
		
		try:
			# Если существует, то выбираем эту страницу
			queryset = paginator.page(page)  
		except PageNotAnInteger:
			# Если None, то выбираем первую страницу
			queryset = paginator.page(1)  
		except EmptyPage:
			# Если вышли за последнюю страницу, то возвращаем последнюю
			queryset = paginator.page(paginator.num_pages) 
		context = {
			"object_list":queryset,
			"title": "List"
			}
		return render(request, 'dumpgal.html', context)

class BestSiteView(ListView):
	model = Best_sites
	template_name = 'best_sites.html'
	def get_context_data(self, *args, **kwargs):
		context = super(BestSiteView, self).get_context_data(*args, **kwargs)
		context['b_sites'] = self.model.objects.all()
		return context


class FHG_modelsView(ListView):	
	def get(self, request):
		dump_list = FHG_models.objects.all()
		paginator = Paginator(dump_list, 24) # Show 42 contacts per page
		page = request.GET.get('page')
		
		try:
			# Если существует, то выбираем эту страницу
			queryset = paginator.page(page)  
		except PageNotAnInteger:
			# Если None, то выбираем первую страницу
			queryset = paginator.page(1)  
		except EmptyPage:
			# Если вышли за последнюю страницу, то возвращаем последнюю
			queryset = paginator.page(paginator.num_pages) 
		context = {
			"object_list":queryset,
			"title": "List"
			}
		return render(request, 'FHG_models.html', context)

class BestModelToday(ListView):
	model = FHG_models
	template_name = 'bumpgal.html'
	def get_context_data(self, *args, **kwargs):
		context = super(BestModelToday, self).get_context_data(*args, **kwargs)
		context['bmts'] = self.model.objects.all()
		return context