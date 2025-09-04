import enum
import uuid
from sqlalchemy import Column, Enum, MetaData, String, Table, Text
from sqlalchemy.dialects.postgresql import UUID


metadata = MetaData()


class StatusEnum(str, enum.Enum):
    created = "создано",
    in_work = "в работе",
    finished = "завершено"


task_table = Table(
    "task",
    metadata,
    Column("uuid", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    Column("name", String(150)),
    Column("description", Text),
    Column("status", Enum(StatusEnum), default=StatusEnum.created)
)
