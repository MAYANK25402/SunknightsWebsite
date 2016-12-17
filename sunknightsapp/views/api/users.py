from rest_framework import viewsets
from ...serializers.clan_user_serializer import ClanUserSerializer
from ...models.clan_user import ClanUser
from rest_framework_bulk import BulkModelViewSet

class ClanUsersViewSet(BulkModelViewSet):
    serializer_class = ClanUserSerializer
    queryset = ClanUser.objects.all()
    lookup_field = 'discord_id'