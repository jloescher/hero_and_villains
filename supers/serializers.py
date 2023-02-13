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

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.alter_ego = validated_data.get("alter_ego", instance.alter_ego)
        instance.primary_ability = validated_data.get(
            "primary_ability", instance.primary_ability
        )
        instance.secondary_ability = validated_data.get(
            "secondary_ability", instance.secondary_ability
        )
        instance.catchphrase = validated_data.get("catchphrase", instance.catchphrase)
        instance.super_type = validated_data.get("super_type", instance.super_type)
        instance.save()
        return instance
