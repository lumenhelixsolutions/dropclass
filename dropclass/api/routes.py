"""Formation API routes — mounted by Atelier shell."""

from fastapi import APIRouter

from dropclass.discovery.classcentral import search_courses
from dropclass.formation.store import FormationStore

router = APIRouter(tags=["formation"])
store = FormationStore()


@router.get("/status")
async def formation_status() -> dict:
    return {
        "engine": "dropclass",
        "enrollments": len(store.list_enrollments()),
    }


@router.get("/discover")
async def discover(subject: str, limit: int = 10) -> dict:
    courses = await search_courses(subject, limit=limit)
    return {"subject": subject, "courses": courses}