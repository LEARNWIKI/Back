from loguru import logger

from lw_main.models import User, Project, Node, Edge


def run():
    logger.warning("ВНИМАНИЕ, ПРОИЗОЙДЁТ УДАЛЕНИЕ ДАННЫХ ИЗ БАЗЫ ДАННЫХ, НАЖМИТЕ ENTER ДЛЯ ПРОДОЛЖЕНИЯ")
    input()

    User.objects.all().delete()
    test_user = User.create("TeaDove", password="best password ever")
    User.create("TeaSparrow", password="best password ever")
    User.create("MeeKey", password="best password ever")
    User.create("Антон", password="best password ever")
    User.create("Man", password="best password ever")

    project = Project.create(title="Лучшая доска по изучению Питона", user=test_user)
    project2 = Project.create(title="Лучшая доска по изучению Го", user=test_user)
    nodes = [Node.create(title="Питон", project=project),
             Node.create(title="SQL", project=project),
             Node.create(title="ORM", project=project),
             Node.create(title="Типы данных", project=project),
             Node.create(title="Память", project=project),
             Node.create(title="Алгоритмы", project=project),
             Node.create(title="Паника", project=project2)]

    edges = [Edge.create(node_out=nodes[0], node_in=nodes[1]),
             Edge.create(node_out=nodes[2], node_in=nodes[1], is_bidirectional=True),
             Edge.create(node_out=nodes[0], node_in=nodes[5]),
             Edge.create(node_out=nodes[3], node_in=nodes[2]),
             Edge.create(node_out=nodes[4], node_in=nodes[1], is_bidirectional=True),
             Edge.create(node_out=nodes[5], node_in=nodes[0])]