from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from adapters.database.repositories.task_repository import \
    TaskRepository
from application.services.task_service import TaskService
from adapters.database.settings import get_async_session


def create_task_repository(
        session: AsyncSession = Depends(get_async_session),
) -> TaskRepository:
    """Внедрения зависимостей для слоя репозиториев"""
    return TaskRepository(session=session)


def create_task_service(
        task_repository: TaskRepository = Depends(
            create_task_repository),
) -> TaskService:
    """Внедрения зависимостей для слоя сервисов"""
    return TaskService(task_repository=task_repository)
