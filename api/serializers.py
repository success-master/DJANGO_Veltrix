from rest_framework import serializers
from request.models import Request


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request

        fields = (
            'id',
            'content',
            'date_posted',
            'ref_code',
            'author',
            'author_dept',
            'assign_to',
            'editor',
            'time_edited',
            'status',
        )
