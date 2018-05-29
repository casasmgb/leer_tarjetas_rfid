from tastypie.resources import ModelResource
from api.models import Tarjeta

class TarjetaResource(ModelResource):
    class Meta:
        queryset = Tarjeta.objects.all()
        resource_name = 'tarjeta'