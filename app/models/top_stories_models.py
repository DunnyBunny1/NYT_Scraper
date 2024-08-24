from pydantic import BaseModel, Field, field_validator
from datetime import datetime
from pydantic.types import PositiveInt
from typing import List

"""
Models for the NYT `topstories` endpoint 
"""


class Multimedia(BaseModel):
    url: str
    format: str
    height: int
    width: int
    type: str
    subtype: str
    caption: str
    copyright: str


class Article(BaseModel):
    section: str
    subsection: str
    title: str
    abstract: str
    url: str
    uri: str
    byline: str
    item_type: str
    updated_date: str
    created_date: str
    published_date: str
    material_type_facet: str
    kicker: str
    des_facet: List[str]
    org_facet: List[str]
    per_facet: List[str]
    geo_facet: List[str]
    multimedia: List[Multimedia]
    short_url : str


class TopStoriesResponse(BaseModel):
    status: str
    copyright: str
    section: str
    last_updated: datetime
    num_results: PositiveInt
    results: List[Article]

    @field_validator('last_updated',mode='before')
    @classmethod
    def convert_to_datetime(cls, value: str) -> datetime:
        return datetime.fromisoformat(value)
