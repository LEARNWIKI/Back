from django.contrib.auth.models import User as DjangoUser
from django.db import models
from loguru import logger


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)   # DRY not followed
    updated_at = models.DateTimeField(auto_now=True)   # DRY not followed

    # TODO сделать полноценный абстрактынй __str__
    def __str__(self):
        """
        Выдаёт поля объекта и их значения, публичные и не вызываемые.
        """
        # fields_dict = {field: getattr(self, field) for field in dir(self) if not field.startswith('_')
        #                and not callable(getattr(self, field)) and field not in ["query", "registry", 'metadata']}
        return self.__class__.__name__ # + ": " + str(fields_dict)

    def _log(self):
        logger.info('instance "{}" of "{}" created'.format(self, self.__class__.__name__))

    class Meta:
        abstract = True


class User(BaseModel, DjangoUser):
    pass


class Project(BaseModel):
    title = models.TextField()
    description = models.TextField(null=True)
    # TODO использовать более оптимальные типы
    edge_properties = models.JSONField(null=True)
    node_properties = models.JSONField(null=True)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)


class Node(BaseModel):
    title = models.TextField(null=True)
    # TODO продумать как будут храниться данные внутри нод
    properties = models.JSONField(null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)


class Edge(BaseModel):
    # TODO продумать как будут храниться данные внутри еджей, скорее всего массив
    properties = models.JSONField(null=True)
    direction = models.CharField(max_length=32)
    node_1 = models.ForeignKey(Node, on_delete=models.CASCADE, null=True, related_name='node_1')
    node_2 = models.ForeignKey(Node, on_delete=models.CASCADE, null=True, related_name='node_2')


class Links(BaseModel):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    url = models.TextField()
    right = models.CharField(max_length=32)

