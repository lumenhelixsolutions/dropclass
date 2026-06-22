"""Class Central discovery — catalog search (MVP: structured stub + HTTP fetch path)."""

from __future__ import annotations

import logging
from typing import Any

import httpx

logger = logging.getLogger(__name__)

CLASSCENTRAL_SEARCH = "https://www.classcentral.com/search"


async def search_courses(subject: str, limit: int = 10) -> list[dict[str, Any]]:
    """
    Return course candidates for a subject.

    MVP returns normalized stubs; Phase 1 adds HTML parse of Class Central results
    filtered to Coursera + free audit where possible.
    """
    subject = subject.strip()
    if not subject:
        return []

    # Placeholder until HTML parser ships — proves API contract for Atelier UI.
    return [
        {
            "title": f"{subject.title()} — candidate {i + 1}",
            "provider": "coursera",
            "catalog_url": CLASSCENTRAL_SEARCH,
            "audit_free": None,
            "cert_eligible": None,
            "note": "MVP stub — wire Class Central parse in IU-2",
        }
        for i in range(min(limit, 3))
    ]


async def fetch_search_page(subject: str) -> str:
    """Fetch raw Class Central search HTML (for parser tests)."""
    params = {"q": subject}
    async with httpx.AsyncClient(timeout=20.0, follow_redirects=True) as client:
        resp = await client.get(CLASSCENTRAL_SEARCH, params=params)
        resp.raise_for_status()
        return resp.text