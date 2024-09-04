from rest_framework import generics

from api.serializers.decrypt_message import DecryptMessageSerializer


class DecryptMessageView(generics.CreateAPIView):
    serializer_class = DecryptMessageSerializer
