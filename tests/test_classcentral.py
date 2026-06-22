import pytest

from dropclass.discovery.classcentral import search_courses


@pytest.mark.asyncio
async def test_search_returns_stub_candidates():
    results = await search_courses("cartography", limit=2)
    assert len(results) == 2
    assert results[0]["provider"] == "coursera"


@pytest.mark.asyncio
async def test_search_empty_subject():
    assert await search_courses("  ") == []