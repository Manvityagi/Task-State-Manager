from django.urls import path

from upload.controllers.upload import (
    UploadStartController,
    UploadPauseController,
    UploadResumeController,
    # UploadRollbackController,
    UploadTerminateController,
)

app_name = "upload"

urlpatterns = [
    path("start", UploadStartController.as_view(), name="upload_start"),
    path("pause", UploadPauseController.as_view(), name="upload_pause"),
    path("resume", UploadResumeController.as_view(), name="upload_resume"),
    path("terminate", UploadTerminateController.as_view(), name="upload_terminate",),
    # path("rollback", UploadRollbackController.as_view(), name="upload_rollback"),
]
