from email.policy import default
from operator import index
from rest_framework import status
from rest_framework.pagination import PageNumberPagination

from rest_framework.response import Response

class CustomPagination(PageNumberPagination):
    page_size=3
    page_size_query_param='page_size'

    def get_paginated_response(self, data):
        return Response({
                'totalRecords': self.page.paginator.count,
                "pageIndex":self.page.number,
                'data' : data
        })