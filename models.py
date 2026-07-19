from pydantic import BaseModel

class MeetingRequest(BaseModel):
    notes: str


class MeetingResponse(BaseModel):
    summary: str
    action_items: list[str]
    decisions: list[str]
    risks: list[str]
