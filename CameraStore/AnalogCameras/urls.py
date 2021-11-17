from django.urls import path, include
from .views import CRUDCamera, CRUDFilmCamera, CRUDItemsCamera, CRUDTechnicalSupport, CRUDClient, CRUDLeasing, CRUDModelCamera
from django.views.generic import TemplateView
# from rest_framework.routers import DefaultRouter
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html")),

    path('camera/list/', TemplateView.as_view(template_name="camera_list.html")),
    path('camera/add/', TemplateView.as_view(template_name="camera_create.html")),
    path('camera/<int:pk>/edit/', TemplateView.as_view(template_name="camera_edit.html")),
    path('camera/<int:pk>/delete/', TemplateView.as_view(template_name="camera_delete.html")),

    path('api/camera/new/', csrf_exempt(CRUDCamera.as_view())),
    path('api/camera/all/', csrf_exempt(CRUDCamera.as_view())),
    path('api/camera/<int:pk>/', csrf_exempt(CRUDCamera.as_view())),

    path('filmcamera/list/', TemplateView.as_view(template_name="filmcamera_list.html")),
    path('filmcamera/add/', TemplateView.as_view(template_name="filmcamera_create.html")),
    path('filmcamera/<int:pk>/delete/', TemplateView.as_view(template_name="filmcamera_delete.html")),
    path('filmcamera/<int:pk>/edit/', TemplateView.as_view(template_name="filmcamera_edit.html")),

    path('api/filmcamera/new/', csrf_exempt(CRUDFilmCamera.as_view())),
    path('api/filmcamera/all/', csrf_exempt(CRUDFilmCamera.as_view())),
    path('api/filmcamera/<int:pk>/', csrf_exempt(CRUDFilmCamera.as_view())),

    path('technicalsupport/list/', TemplateView.as_view(template_name="technicalsupport_list.html")),
    path('technicalsupport/add/', TemplateView.as_view(template_name="technicalsupport_create.html")),
    path('technicalsupport/<int:pk>/edit/', TemplateView.as_view(template_name="technicalsupport_edit.html")),
    path('technicalsupport/<int:pk>/delete/', TemplateView.as_view(template_name="technicalsupport_delete.html")),

    path('api/technicalsupport/new/', csrf_exempt(CRUDTechnicalSupport.as_view())),
    path('api/technicalsupport/all/', csrf_exempt(CRUDTechnicalSupport.as_view())),
    path('api/technicalsupport/<int:pk>/', csrf_exempt(CRUDTechnicalSupport.as_view())),

    path('itemscamera/list/', TemplateView.as_view(template_name="itemscamera_list.html")),
    path('itemscamera/add/', TemplateView.as_view(template_name="itemscamera_create.html")),
    path('itemscamera/<int:pk>/edit/', TemplateView.as_view(template_name="itemscamera_edit.html")),
    path('itemscamera/<int:pk>/delete/', TemplateView.as_view(template_name="itemscamera_delete.html")),

    path('api/itemscamera/new/', csrf_exempt(CRUDItemsCamera.as_view())),
    path('api/itemscamera/all/', csrf_exempt(CRUDItemsCamera.as_view())),
    path('api/itemscamera/<int:pk>/', csrf_exempt(CRUDItemsCamera.as_view())),

    path('client/add/', TemplateView.as_view(template_name="client_create.html")),
    path('client/list/', TemplateView.as_view(template_name="client_list.html")),
    path('client/<int:pk>/edit/', TemplateView.as_view(template_name="client_edit.html")),
    path('client/<int:pk>/delete/', TemplateView.as_view(template_name="client_delete.html")),

    path('api/client/new/', csrf_exempt(CRUDClient.as_view())),
    path('api/client/all/', csrf_exempt(CRUDClient.as_view())),
    path('api/client/<int:pk>/', csrf_exempt(CRUDClient.as_view())),

    path('leasing/add/', TemplateView.as_view(template_name="leasing_create.html")),
    path('leasing/list/', TemplateView.as_view(template_name="leasing_list.html")),
    path('leasing/<int:pk>/edit/', TemplateView.as_view(template_name="leasing_edit.html")),
    path('leasing/<int:pk>/delete/', TemplateView.as_view(template_name="leasing_delete.html")),

    path('api/leasing/new/', csrf_exempt(CRUDLeasing.as_view())),
    path('api/leasing/all/', csrf_exempt(CRUDLeasing.as_view())),
    path('api/leasing/<int:pk>/', csrf_exempt(CRUDLeasing.as_view())),

    path('api/modelcamera/new/', csrf_exempt(CRUDModelCamera.as_view())),
    path('api/modelcamera/all/', csrf_exempt(CRUDModelCamera.as_view())),
    path('api/modelcamera/<int:pk>/', csrf_exempt(CRUDModelCamera.as_view())),
]
