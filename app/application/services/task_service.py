from attr import frozen

from application.interfaces.task_interface import TaskInterface
from routing.schemas.task_schemas import (
    TaskCreateSchema,
    TaskSchema, TaskUpdateSchema)


@frozen
class TaskService:
    """Сервис для задачи"""
    task_repository: TaskInterface

    async def get_tasks(self) -> list[TaskSchema]:
        """Метод для получения задач"""
        results = await self.task_repository.get_tasks()
        return [TaskSchema(
            uuid=result.uuid,
            name=result.name,
            description=result.description,
            status=result.status
        ) for result in results]

    async def get_task(self, task_uuid: str) -> TaskSchema | None:
        """Метод для получения задачи по uuid"""
        result = await self.task_repository.get_task(
            task_uuid=task_uuid
        )
        return TaskSchema(
            uuid=result.uuid,
            name=result.name,
            description=result.description,
            status=result.status
        ) if result else None

    async def create_task(
        self,
        create_data: TaskCreateSchema,
    ) -> TaskSchema:
        """Метод для создания задачи"""
        result = await self.task_repository.create_task(
            create_data=create_data
        )
        return TaskSchema(
            uuid=result.uuid,
            name=result.name,
            description=result.description,
            status=result.status
        )

    async def update_task(
        self,
        task_uuid: str,
        update_data: TaskUpdateSchema,
    ) -> TaskSchema:
        """Метод для изменения задачи по uuid"""
        result = await self.task_repository.update_task(
            task_uuid=task_uuid,
            update_data=update_data
        )
        return TaskSchema(
            uuid=result.uuid,
            name=result.name,
            description=result.description,
            status=result.status
        )
