"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rmsApp.views import indexPage, ReportDetailsListView, ReportDetailsCreateView, ReportDetailsUpdateView, ReportDetailsDeleteView, download_catalog_pdf

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', indexPage, name='index'),
    path('reports/', ReportDetailsListView.as_view(), name='ReportDetails'),
    path('add-report/', ReportDetailsCreateView.as_view(), name='AddReport'),
    path('edit-report/<int:pk>/', ReportDetailsUpdateView.as_view(), name='EditReport'),
    path('delete-report/<int:pk>/', ReportDetailsDeleteView.as_view(), name='DeleteReport'),
    path('download_catalog_pdf/', download_catalog_pdf, name='DownloadCatalogPDF'),
]
