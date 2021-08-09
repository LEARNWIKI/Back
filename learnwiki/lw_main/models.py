from django.contrib.auth.models import User as DjangoUser
from django.db import models
from loguru import logger


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Выдаёт поля объекта и их значения, публичные и не вызываемые.
        """
        fields_dict = {field: getattr(self, field) for field in self.__dict__ if not field.startswith('_')
                       and not callable(getattr(self, field))
                       and field not in ['DoesNotExist', 'EMAIL_FIELD', 'Meta', 'MultipleObjectsReturned',
                                         'REQUIRED_FIELDS', 'USERNAME_FIELD']}
        return self.__class__.__name__ + ": " + str(fields_dict)

    def _log(self):
        logger.info(str(self))

    class Meta:
        abstract = True


class User(BaseModel, DjangoUser):
    pass


class Project(BaseModel):
    title = models.TextField()
    description = models.TextField(null=True)
    is_public = models.BooleanField(default=False)
    # TODO использовать более оптимальные типы
    edge_properties = models.JSONField(null=True)
    node_properties = models.JSONField(null=True)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name="projects")


class Node(BaseModel):
    title = models.TextField(null=True)
    # TODO продумать как будут храниться данные внутри нод
    properties = models.JSONField(null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="nodes")

    def get_all_edges(self):
        nodes1 = [node for node in self.edges_out.all()]
        nodes2 = [node for node in self.edges_in.all()]
        return nodes1 + nodes2


class Edge(BaseModel):
    # TODO продумать как будут храниться данные внутри еджей, скорее всего массив
    properties = models.JSONField(null=True)
    is_bidirectional = models.BooleanField(default=False)
    # TODO тригер на запрет ссылок на одну и ту же ноду(хотя может и не надо)
    node_out = models.ForeignKey(Node, on_delete=models.CASCADE, related_name='edges_out')
    node_in = models.ForeignKey(Node, on_delete=models.CASCADE, related_name='edges_in')


class Links(BaseModel):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="links")
    url = models.TextField()
    right = models.CharField(max_length=32)

