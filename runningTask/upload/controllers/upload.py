from threading import Thread

from rest_framework.response import Response
from rest_framework.views import APIView

from upload.managers.upload import UploadManager

global manager


class UploadStartController(APIView):
    """Controller for starting upload for a given user id."""

    def post(self, request):
        """Method to start upload of a csv file into the database.
        
        Args: 
            request: A Django HTTP request object.
        
        Returns:
            Response with Status : Upload Started
        """
        data = request.data
        global userId
        userId = data["userid"]

        global manager
        manager = UploadManager(userId)

        thread = Thread(manager.start())
        thread.start()

        return Response("Status : Upload Started")


class UploadPauseController(APIView):
    """Controller for pausing upload"""

    def post(self, request):
        """Method to pause upload of a csv file being uploaded into the database.
        
        Args: 
            request: A Django HTTP request object.
        
        Returns:
            Response with Status : Upload Paused
        """
        global manager
        manager.pause()
        return Response("Status : Upload Paused")


class UploadResumeController(APIView):
    """Controller for resuming upload"""

    def post(self, request):
        """Method to resume upload of a paused csv file.
        
        Args: 
            request: A Django HTTP request object.
        
        Returns:
            Response with Status : Upload Resumed
        """
        global manager
        manager.resume()
        return Response("Status : Upload Resumed")


class UploadTerminateController(APIView):
    """Controller for terminating upload"""

    def post(self, request):
        """Method to terminate and rollback upload of a csv file.
        
        Args: 
            request: A Django HTTP request object.
        
        Returns:
            Response with Status : Upload Terminated
        """
        global manager
        manager.terminate()
        return Response("Status : Upload Terminated")


class UploadProgressController(APIView):
    def get(self, request):
        pass
