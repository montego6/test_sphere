from email import message
from django.db.migrations import serializer
import graphene
from graphene.types.scalars import Scalar
from graphene_django import DjangoObjectType
from graphene_django.rest_framework.mutation import SerializerMutation
from main.serializers import CarPassSerializer
from .models import CarPass

class ObjectField(Scalar): 
    @staticmethod
    def serialize(dt):
        return dt 

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
    

class CreateCar(graphene.Mutation):
    car_pass = graphene.Field(CarPassType)
    message = ObjectField()
    status = graphene.Int()

    class Arguments:
        brand = graphene.String(required=True)
        model = graphene.String(required=True)
        plate_number = graphene.String(required=True)
        owners_name = graphene.String(required=True)

    @classmethod
    def mutate(cls, root, info, **kwargs):
        serializer = CarPassSerializer(data=kwargs)
        if serializer.is_valid():
            obj=serializer.save()
            msg='success'
            status = 201
        else:
            msg=serializer.errors
            obj=None
            status = 400
        return cls(car_pass=obj,message=msg,status=status)


class UpdateCar(graphene.Mutation):
    car_pass = graphene.Field(CarPassType)
    message = ObjectField()
    status = graphene.Int()

    class Arguments:
        id = graphene.ID(required=True)
        brand = graphene.String()
        model = graphene.String()
        plate_number = graphene.String()
        owners_name = graphene.String()

    @classmethod
    def mutate(cls, root, info, id, **kwargs):
        car = CarPass.objects.get(id=id)
        serializer = CarPassSerializer(car, data=kwargs, partial=True)
        if serializer.is_valid():
            obj=serializer.save()
            msg='success'
            status = 201
        else:
            msg=serializer.errors
            obj=None
            status = 400
        return cls(car_pass=obj,message=msg,status=status)


class Mutation(graphene.ObjectType):
    create_car = CreateCar.Field()
    update_car = UpdateCar.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)