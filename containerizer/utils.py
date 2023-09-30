import docker
from .models import RunningHistoryRecord, Container



def run(app):
    client = docker.from_env()
    container = client.containers.run(
                                    image=app.image_address, 
                                    command=app.command, 
                                    environment=app.envs, 
                                    detach=True
                                )
    return container.id


def stop(container_id):
    client = docker.from_env()
    container = client.containers.get(container_id)
    container.stop()
    container.remove()


def record_history(container: Container, status):

    record_obj = RunningHistoryRecord.objects.create(
                                                container=container,
                                                status=status,
                                                envs = container.app.envs
                                            )
    
    return record_obj