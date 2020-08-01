from rest_framework.views import APIView
from rest_framework.response import Response
from threading import Thread

roll_back_checkpoint = None


class UploadTryController(APIView):
    def get(self, request):
        print("Trying the connections")
        return Response("GOD")


class UploadStartController(APIView):
    """Controller for starting upload
    """

    def post(self, request):
        print("Hello Start")
        return Response()


class UploadPauseController(APIView):
    def post(self, request):
        pass


class UploadResumeController(APIView):
    def post(self, request):
        pass


class UploadTerminateController(APIView):
    def get(self, request):
        pass


class UploadProgressController(APIView):
    def get(self, request):
        pass

