from graphene_django import DjangoObjectType, DjangoListField
from Contents.models import User, Content


class ContentType(DjangoObjectType):
    class Meta:
        model = Content
        fields = ("id", "heading", "content_data", "user", "created_at")


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ("id", "name", "details")

    contents = DjangoListField(ContentType)

    def resolve_contents(self, info):
        return Content.objects.filter(user=self.id)
