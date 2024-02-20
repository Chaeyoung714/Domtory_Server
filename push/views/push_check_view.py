from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from push.containers import PushContainer
from drf_yasg.utils import swagger_auto_schema
from push.serializers import PushCheckRequestSerialzier
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from drf_yasg import openapi

authorization_header = openapi.Parameter(
    'Authorization', 
    openapi.IN_HEADER, 
    description="Bearer <token>", 
    type=openapi.TYPE_STRING,
    required=True
)

class PushCheckView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._push_service = PushContainer.push_service()

    @swagger_auto_schema(manual_parameters=[authorization_header], request_body=PushCheckRequestSerialzier,responses={"200": ""})
    def put(self, request):
        """
        푸시 알림 기록을 본 직후 불러와서 isChecked를 True로 바꿔주는 api 입니다.
        """
        self._push_service.check_push_notification(request.data)
        return Response(status=status.HTTP_200_OK)