from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField



status = (
        ("Running", "Running"),
        ("Finished", "Finished"),
    )


class App(models.Model):
    name = models.CharField(max_length=255)
    image_address = models.CharField(max_length=255)
    envs = models.JSONField(blank=True, null=True)
    command = ArrayField(models.CharField(max_length=255))
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
       indexes = [
           models.Index(fields=['id']),]

    def __str__(self):
        return self.name


class Container(models.Model):
    container_id = models.CharField(max_length=255, unique=True)
    app = models.ForeignKey(App, on_delete=models.CASCADE, related_name='apps')
    created_at = models.DateTimeField(auto_now_add=True)
    stopped_at = models.DateTimeField(blank=True, null=True)

    class Meta:
       indexes = [
           models.Index(fields=['container_id']),]

    def __str__(self):
        return self.app.name + " : " + self.container_id
    


class RunningHistoryRecord(models.Model):
    container = models.ForeignKey(
                            Container, 
                            to_field='container_id', 
                            db_column='container_id', 
                            on_delete=models.CASCADE, 
                            related_name="containers"
                        )
    status = models.CharField(max_length=255, choices=status)
    envs = models.JSONField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
       indexes = [
           models.Index(fields=['container_id']),]