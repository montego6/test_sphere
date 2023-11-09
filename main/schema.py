import graphene
from graphene_django import DjangoObjectType
from .models import CarPass

class CarPassType(DjangoObjectType):
    class Meta:
        model = CarPass
        fields = ('id', 'uuid', 'brand', 'model', 'plate_number', 'owners_name', 'created_at', 'updated_at')

class Query(graphene.ObjectType):
    all_cars = graphene.List(CarPassType)
    car_by_id = graphene.Field(CarPassType, id=graphene.String())

    def resolve_all_cars(root, info):
        return CarPass.objects.all()
    
    def resolve_car_by_id(root, info, id):
        return CarPass.objects.get(pk=id)
    

class CarCreateMutation(graphene.Mutation):
    


schema = graphene.Schema(query=Query)