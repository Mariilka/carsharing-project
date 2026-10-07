from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins, viewsets



from carsharing.models import Category, Client, Car, Region, Rental
from carsharing.serializers import CategorySerializer, ClientSerializer, CarSerializer, RegionSerializer, RentalSerializer


class CategoryViewset(mixins.ListModelMixin, GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
class ClientViewset(mixins.ListModelMixin, GenericViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
class CarViewset(mixins.ListModelMixin, GenericViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
class RegionViewset(mixins.ListModelMixin, GenericViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
class RentalViewset(mixins.ListModelMixin, GenericViewSet):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer

