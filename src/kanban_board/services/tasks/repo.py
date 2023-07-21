from abc import ABC, abstractmethod

from django.contrib.auth import get_user_model
from django.db.models import QuerySet

from kanban_board.models import Task, KanbanBoard
from kanban_board.services.tasks.entries import CreateTaskEntry



User = get_user_model()


class TaskRepo(ABC):
    qs = Task.objects.all()

    @abstractmethod
    def all(self) -> QuerySet[Task]: ...

    @abstractmethod
    def create(self, user: User, board: KanbanBoard, board_data: CreateTaskEntry) -> Task: ...

    @abstractmethod
    def set_performers(self, task: Task, performers: QuerySet[User]) -> None: ...
