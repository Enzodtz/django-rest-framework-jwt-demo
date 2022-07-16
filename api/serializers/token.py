from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super(CustomTokenObtainPairSerializer, self).validate(attrs)

        data.update({"id": self.user.id})
        data.update({"email": self.user.email})
        data.update({"name": self.user.name})
        # data.update({"userFirstName": self.user.first_name})
        # data.update({"userLastName": self.user.last_name})
        # data.update({"userCellphone": self.user.cellphone})

        return data
