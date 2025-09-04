from fastapi import APIRouter, Depends, HTTPException

from routing.schemas.task_schemas import (
    TaskCreateSchema, TaskSchema, TaskUpdateSchema)
from application.services.task_service import TaskService
from adapters.depends.task_depends import create_task_service

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.get(
    "/",
    responses={400: {"description": "Bad request"}},
    response_model=list[TaskSchema],
    description="Получение списка всех задач",
)
async def get_all_tasks(
    task_service: TaskService = Depends(create_task_service),
) -> list[TaskSchema]:
    """Метод для получения задач"""
    tasks = await task_service.get_tasks()
    return tasks


@router.get(
    "/{task_uuid}",
    responses={400: {"description": "Bad request"}},
    response_model=TaskSchema,
    description="Получение задачи по uuid",
)
async def get_task(
    task_uuid: str,
    task_service: TaskService = Depends(create_task_service),
) -> TaskSchema:
    """Метод для получения задачи по uuid"""
    task = await task_service.get_task(task_uuid=task_uuid)
    if not task:
        raise HTTPException(status_code=404, detail="task not found")
    return task


@router.post(
    "/",
    responses={400: {"description": "Bad request"}},
    response_model=TaskSchema,
    description="Создание задачи",
    status_code=201,
)
async def post_create_task(
    create_data: TaskCreateSchema,
    task_service: TaskService = Depends(create_task_service),
) -> TaskSchema:
    """Метод для создания задачи"""
    task = await task_service.create_task(
        create_data=create_data
    )
    return task

@router.patch(
    "/{task_uuid}",
    responses={400: {"description": "Bad request"}},
    response_model=TaskSchema,
    description="Получение задачи по uuid",
)
async def update_task(
    task_uuid: str,
    update_data: TaskUpdateSchema,
    task_service: TaskService = Depends(create_task_service),
) -> TaskSchema:
    """Метод для изменения задачи по uuid"""
    task = await task_service.update_task(
        task_uuid=task_uuid,
        update_data=update_data
    )
    if not task:
        raise HTTPException(status_code=404, detail="task not found")
    return task
