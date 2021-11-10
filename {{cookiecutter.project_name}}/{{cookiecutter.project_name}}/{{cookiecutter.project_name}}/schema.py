import graphene
from graphene_django import DjangoObjectType

from {{cookiecutter.app_name}}.models import Test


class TestType(DjangoObjectType):
    class Meta:
        model = Test
        fields = ("id", "name", "size", "consumers")


class CreateTest(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()
    size = graphene.Int()
    consumers = graphene.String()

    class Arguments:
        name = graphene.String()
        size = graphene.Int()
        consumers = graphene.String()

    def mutate(self, info, name, size, status):
        test = Test(name=name, size=size, consumers=consumers)
        test.save()

        return CreateTest(
            id=test.id,
            name=test.name,
            size=test.size,
            consumers=test.consumers,
        )

class MutateTest(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        name = graphene.String()
        size = graphene.Int()
        consumers = graphene.String()

    test = graphene.Field(TestType)
    
    @classmethod
    def mutate(cls, root, info, id,
               name,
               size,
               consumers
        ):
        t = Test.objects.get(pk=id)
        t.name = name;
        t.size = size;
        t.consumers = consumers;
        t.save()
        
        return MutateTest(test=t)


class Mutation(graphene.ObjectType):
    update_test = MutateTest.Field()

class Query(graphene.ObjectType):
    all_test = graphene.List(TestType)
    
    def resolve_all_tests(root, info):
        return Test.objects.all()

    def resolve_test_by_name(root, info, name):
        try:
            return Test.objects.get(name=name)
        except Test.DoesNotExist:
            return None

schema = graphene.Schema(
    query=Query,
    mutation=Mutation,
    # subscriptions
)