from threading import Thread

from rest_framework.response import Response
from rest_framework.views import APIView

from upload.managers.upload import UploadManager

roll_back_checkpoint = None
userId = None


class UploadStartController(APIView):
    """Controller for starting upload
    """

    def post(self, request):
        data = request.data
        global userId
        userId = data["userid"]

        global roll_back_checkpoint
        manager = UploadManager(userId)

        thread = Thread(manager.start())
        thread.start()

        # roll_back_checkpoint = manager.get_checkpoint()

        return Response("Status : Thread Started")


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
