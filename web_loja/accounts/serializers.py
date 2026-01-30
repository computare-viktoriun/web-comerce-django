from rest_framework import serializers
from accounts.models import BaseUser

class BaseUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseUser
        fields = [
            'id',
            'username',
            'email',
            'password',
            'idade',
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = BaseUser(**validated_data)
        user.set_password(password)  # 🔐 hash correto
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if password:
            instance.set_password(password)  # 🔐 atualiza senha corretamente

        instance.save()
        return instance
