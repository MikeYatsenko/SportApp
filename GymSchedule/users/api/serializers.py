from rest_framework import  serializers
from users.models import SiteUser

class UserDisplaySerializer(serializers.ModelSerializer):
  class Meta:
      model = SiteUser
      fields = ["username"]