import graphene
from graphene_django.filter import DjangoFilterConnectionField
from .types import UserType, ContentType
from .mutations import Mutation


class Query(graphene.ObjectType):
    user_contents = DjangoFilterConnectionField(ContentType)
    content = graphene.relay.Node.Field(ContentType)
    user = graphene.relay.Node.Field(UserType)
    all_users = DjangoFilterConnectionField(UserType)


schema = graphene.Schema(query=Query, mutation=Mutation)
