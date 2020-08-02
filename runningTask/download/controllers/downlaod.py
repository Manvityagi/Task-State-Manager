from threading import Thread

from rest_framework.response import Response
from rest_framework.views import APIView

from download.managers.download import DownloadManager

global manager

class DownloadStartController(APIView):
    """Controller for starting Download
    """

    def post(self, request):
        data = request.data
        global userId
        userId = data["userid"]

        global manager
        manager = DownloadManager(userId)

        thread = Thread(manager.start())
        thread.start()

        return Response("Status : Download Started")


class DownloadPauseController(APIView):
    def post(self, request):
        global manager
        manager.pause()
        return Response("Status : Download Paused")


class DownloadResumeController(APIView):
    def post(self, request):
        global manager
        manager.resume()
        return Response("Status : Download Resumed")


class DownloadTerminateController(APIView):
    def post(self, request):
        global manager
        manager.terminate()
        return Response("Status : Download Terminated")

class DownloadProgressController(APIView):
    def get(self, request):
        pass
