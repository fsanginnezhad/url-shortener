from rest_framework import serializers
from .models import Link

class LinkSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    original_url = serializers.URLField(max_length=2000)
    short_code = serializers.CharField(max_length=10, read_only=True)
    is_active = serializers.BooleanField(default=True)
    click_count = serializers.IntegerField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    expires_at = serializers.DateTimeField(required=False, allow_null=True)

    def create(self, validated_data):
        owner = self.context['request'].user
        return Link.objects.create(owner=owner, **validated_data)

    def update(self, instance, validated_data):
        instance.original_url = validated_data.get('original_url', instance.original_url)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.expires_at = validated_data.get('expires_at', instance.expires_at)
        instance.save()
        return instance

    def validate_orginal_url(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("آدرس خیلی کوتاه است")
        return value