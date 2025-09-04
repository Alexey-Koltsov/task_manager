from sqlalchemy.orm import registry, relationship

from adapters.database.tables import task_table
from application.dataclasses.dataclasses import Task

mapper_registry = registry()


mapper_registry.map_imperatively(
    Task,
    task_table,
)
