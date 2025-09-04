from typing import Optional

from pydantic import BaseModel
from uuid import UUID

from adapters.database.tables import StatusEnum


class TaskCreateSchema(BaseModel):
    """
    Схема для создания задачи.

    Attributes:
        name (str): Название задачи.
        description (str): Описание задачи.
    """
    name: str
    description: str


class TaskSchema(TaskCreateSchema):
    """
    Схема для представления задачи.
    Наследует атрибуты из TaskCreateSchema и добавляет уникальный
    идентификатор.

    Attributes:
        uuid (UUID): Уникальный идентификатор задачи.
        name (str): Название задачи.
        description (str): Описание задачи.
        status (StatusEnum): Статус задачи.
    """
    uuid: UUID
    status: StatusEnum


class TaskUpdateSchema(BaseModel):
    """Схема для частичного обновления задачи.
        Attributes:
        name (str): Название задачи.
        description (str): Описание задачи.
        status (StatusEnum): Статус задачи.
    """
    name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[StatusEnum] = None
