from rest_framework import serializers
from .models import Super


class SuperSerializer(serializers.ModelSerializer):
    super_type = serializers.ChoiceField(choices=Super.SUPER_TYPE_CHOICES)

    class Meta:
        model = Super
        fields = [
            "name",
            "alter_ego",
            "primary_ability",
            "secondary_ability",
            "catchphrase",
            "super_type",
        ]
        partial = True

    def create(self, validated_data):
        super_obj = Super.objects.create(**validated_data)
        return super_obj
