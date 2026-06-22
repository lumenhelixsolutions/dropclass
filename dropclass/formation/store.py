"""Formation enrollment state — in-memory MVP; SQLite in IU-3."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any
import time
import uuid


@dataclass
class Enrollment:
    id: str
    course_title: str
    coursera_url: str
    status: str = "pending"
    progress: float = 0.0
    created_at: float = field(default_factory=time.time)
    meta: dict[str, Any] = field(default_factory=dict)


class FormationStore:
    def __init__(self) -> None:
        self._enrollments: dict[str, Enrollment] = {}

    def create(self, course_title: str, coursera_url: str) -> Enrollment:
        eid = str(uuid.uuid4())
        enrollment = Enrollment(id=eid, course_title=course_title, coursera_url=coursera_url)
        self._enrollments[eid] = enrollment
        return enrollment

    def list_enrollments(self) -> list[Enrollment]:
        return list(self._enrollments.values())

    def get(self, enrollment_id: str) -> Enrollment | None:
        return self._enrollments.get(enrollment_id)