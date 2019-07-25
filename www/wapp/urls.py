
from django.urls import  path
from . import views
from wapp.views import PagView, BestSiteView, FHG_modelsView



urlpatterns = [
	path('', PagView.as_view(), name="index"),
	path('Best_sites', BestSiteView.as_view(), name = 'Best_sites'),	
	path('Models', FHG_modelsView.as_view(), name = 'models'),
]
