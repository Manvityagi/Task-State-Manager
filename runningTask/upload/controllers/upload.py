from threading import Thread

from rest_framework.response import Response
from rest_framework.views import APIView

from upload.managers.upload import UploadManager

global manager

class UploadStartController(APIView):
    """Controller for starting upload
    """

    def post(self, request):
        data = request.data
        global userId
        userId = data["userid"]

        global manager
        manager = UploadManager(userId)

        thread = Thread(manager.start())
        thread.start()

        return Response("Status : Upload Started")


class UploadPauseController(APIView):
    def post(self, request):
        global manager
        manager.pause()
        return Response("Status : Upload Paused")


class UploadResumeController(APIView):
    def post(self, request):
        global manager
        manager.resume()
        return Response("Status : Upload Resumed")


class UploadTerminateController(APIView):
    def post(self, request):
        global manager
        manager.terminate()
        return Response("Status : Upload Terminated")

class UploadProgressController(APIView):
    def get(self, request):
        pass
