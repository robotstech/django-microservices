from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ("-created_at",)


class Comment(BaseModel):
    body = models.TextField()
    board_id = models.BigIntegerField(unique=True)


class CommentImage(BaseModel):
    image_id = models.BigIntegerField(unique=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="images")

    class Meta:
        unique_together = ('image_id', 'comment')

