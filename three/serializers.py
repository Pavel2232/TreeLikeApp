from rest_framework import serializers
from three.models import Page


class PageSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    class Meta:
        model = Page
        fields = ['name', 'slug', 'url', 'children']

    def get_children(self, obj):
        children = obj.children.all()
        if children:
            serializer = self.__class__(children, many=True)
            return serializer.data
        else:
            return []
