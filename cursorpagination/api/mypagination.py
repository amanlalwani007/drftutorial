from rest_framework.pagination import CursorPagination


class MypageNumberPagination(CursorPagination):
    page_size = 3
    ordering = 'name'
