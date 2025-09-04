from attr import dataclass


@dataclass
class Task:
    """Модель задачи"""
    name: str
    description: str
    status: str
    uuid: str | None = None
