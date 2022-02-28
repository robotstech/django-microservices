from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ("-created_at",)


class Board(BaseModel):
    title = models.CharField(max_length=128)
    body = models.TextField()


class BoardImage(BaseModel):
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name="images")
    image_id = models.PositiveBigIntegerField()
