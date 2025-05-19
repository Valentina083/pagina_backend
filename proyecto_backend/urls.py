"""
URL configuration for proyecto_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from carrito.views import CarritoViewSet
from productos.views import CategoriaViewSet
from productos.views import ProductoViewSet
from usuarios.views import UsuarioViewSet
from facturas.views import FacturaViewSet, DetalleFacturaViewSet

router = DefaultRouter()
router.register('carrito', CarritoViewSet, 'view_carrito')
router.register('categorias', CategoriaViewSet, 'view_categoria')
router.register('productos', ProductoViewSet, 'view_producto')
router.register('usuarios', UsuarioViewSet, 'view_usuario')
router.register('facturas', FacturaViewSet, 'view_factura')
router.register('detalles_factura', DetalleFacturaViewSet, 'view_detalles_factura')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
