from abc import ABC, abstractmethod

from application.dataclasses.dataclasses import Task
from routing.schemas.task_schemas import TaskCreateSchema, TaskUpdateSchema


class TaskInterface(ABC):
    """Интерфейс для задачи"""

    @abstractmethod
    async def get_tasks(self) -> list[Task]:
        """Метод для получения задач"""
        pass

    @abstractmethod
    async def get_task(self, task_uuid: str) -> Task | None:
        """Метод для получения задачи по uuid"""
        pass

    @abstractmethod
    async def create_task(
        self,
        create_data: TaskCreateSchema,
    ) -> Task:
        """Метод для создания задачи"""
        pass

    @abstractmethod
    async def update_task(
        self,
        task_uuid: str,
        update_data: TaskUpdateSchema,
    ) -> Task | None:
        """Метод для изменения задачи по uuid"""
        pass
