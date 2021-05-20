import graphene

from UserContents.types import UserInput, UserType
from Contents.models import User


class AddUser(graphene.Mutation):
    class Arguments:
        input = UserInput(required=True)

    user = graphene.Field(UserType)

    def mutate(parent, info, input=None):
        if input is None:
            return AddUser(user=None)
        _user = User.objects.create(**input)
        return AddUser(user=_user)


class Mutation(graphene.ObjectType):
    add_user = AddUser.Field()
