import uuid
from uuid import UUID

from fastapi import Depends

from app.models.task import Task
from app.repositories.bd_tasks_repo import TaskRepo


class TaskCreationService():
    task_creation_repo: TaskRepo

    def __init__(self, task_creation_repo: TaskRepo = Depends(TaskRepo)) -> None:
        self.task_creation_repo = task_creation_repo

    def get_random_task(self) -> Task:
        return self.task_creation_repo.get_task_by_id(uuid.uuid4())

    def get_n_random_task(self, n: int) -> list[Task]:
        tasks = self.task_creation_repo.get_tasks()
        return [task for task in tasks[:n]]

    def get_task_by_id(self, id: UUID) -> Task:
        return self.task_creation_repo.get_task_by_id(id)








