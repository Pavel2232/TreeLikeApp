from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from three.models import Page
from three.serializers import PageSerializer


class PageAPIView(APIView):

    def get(self, request):
        url = request.query_params.get('url', None)
        if url:

            page = get_object_or_404(Page, url=url)

            serializer = PageSerializer(page)
            return Response(serializer.data)
        else:
            return Response(
                {
                    'error': 'Необходимо указать параметр url'
                },
                status=400
            )
