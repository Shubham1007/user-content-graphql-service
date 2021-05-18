import graphene
from .types import UserType, ContentType
from Contents.models import User, Content


class Query(graphene.ObjectType):
    user_contents = graphene.List(ContentType)
    content = graphene.Field(ContentType, id=graphene.String())
    all_users = graphene.Field(UserType)
    user = graphene.Field(UserType, id=graphene.String())

    def resolve_content_data(parent, info):
        return Content.objects.all().order_by('created_at')

    def resolve_content(parent, info, id):
        return Content.objects.get(id=id)

    def resolve_all_users(parent, info):
        return User.objects.all()

    def resolve_user(parent, info, id):
        return User.objects.get(id=id)


schema = graphene.Schema(query=Query)
