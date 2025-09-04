import logging

from fastapi import HTTPException
from sqlalchemy import insert, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from adapters.database.mapping import Task

from application.interfaces.task_interface import TaskInterface
from routing.schemas.task_schemas import TaskCreateSchema, TaskUpdateSchema

logger = logging.getLogger(__name__)


class TaskRepository(TaskInterface):
    """Репозиторий для задачи"""
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_tasks(self) -> list[Task]:
        """Метод для получения задач"""
        stmt = select(Task)
        results = await self.session.execute(stmt)
        tasks = [Task(
            uuid=result.uuid,
            name=result.name,
            description=result.description,
            status=result.status
        ) for result in results.scalars().all()]

        return tasks

    async def get_task(self, task_uuid: str) -> Task | None:
        """Метод для получения задачи по uuid"""
        stmt = select(Task).where(Task.uuid == task_uuid)
        results = await self.session.execute(stmt)
        result = results.scalars().one_or_none()
        return Task(
            uuid=result.uuid,
            name=result.name,
            description=result.description,
            status=result.status
        ) if result else None

    async def create_task(
            self,
            create_data: TaskCreateSchema,
    ) -> Task:
        """Метод для создания задачи"""
        create_data_dict = create_data.dict()
        stmt = insert(Task).values(**create_data_dict).returning(Task)
        try:
            results = await self.session.execute(stmt)
            result = results.scalars().one_or_none()
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
        task = Task(
            uuid=result.uuid,
            name=result.name,
            description=result.description,
            status=result.status)

        return task

    async def update_task(
            self,
            task_uuid: str,
            update_data: TaskUpdateSchema,
    ) -> Task | None:
        """Метод для изменения задачи по uuid"""
        update_data_dict = {}
        for key, value in update_data.dict().items():
            if value:
                update_data_dict.update({key: value})
        stmt = update(Task).where(Task.uuid == task_uuid).values(
            **update_data_dict).returning(Task) # TODO: попробовать без
        # returning
        try:
            await self.session.execute(stmt)
            await self.session.commit()
            stmt = select(Task).where(Task.uuid == task_uuid)
            results = await self.session.execute(stmt)
            result = results.scalars().one_or_none()
            logger.info(f"Получили задачу {result}")

        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
        task = Task(
            uuid=result.uuid,
            name=result.name,
            description=result.description,
            status=result.status)

        return task
