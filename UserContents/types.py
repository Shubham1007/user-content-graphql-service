import graphene
from graphene import relay
from graphene_django import DjangoObjectType, DjangoListField
from Contents.models import User, Content


class ContentType(DjangoObjectType):
    class Meta:
        model = Content
        fields = ("id", "heading", "content_data", "user", "created_at")
        filter_fields = ['id', 'heading', 'user', 'created_at']
        interfaces = (relay.Node,)


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ("id", "name", "details")
        filter_fields = ['id', 'name', 'details']
        interfaces = (relay.Node,)

    contents = DjangoListField(ContentType)

    def resolve_contents(self, info):
        return Content.objects.filter(user=self.id)


class UserInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String(required=True)
    details = graphene.String()
