from django.urls import path

from download.controllers.download import (
    DownloadStartController,
    DownloadPauseController,
    DownloadResumeController,
    # DownloadRollbackController,
    DownloadTerminateController,
)

app_name = "download"

urlpatterns = [
    path("start", DownloadStartController.as_view(), name="download_start"),
    path("pause", DownloadPauseController.as_view(), name="download_pause"),
    path("resume", DownloadResumeController.as_view(), name="download_resume"),
    path(
        "terminate", DownloadTerminateController.as_view(), name="download_terminate",
    ),
    # path("rollback", DownloadRollbackController.as_view(), name="Download_rollback"),
]
