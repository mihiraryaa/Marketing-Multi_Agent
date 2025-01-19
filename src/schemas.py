from typing import List, Optional
from pydantic import BaseModel,Field, HttpUrl

class campaign_ideas(BaseModel):
    '''
    list of all the campaign ideas with short description of each
    '''
    ideas: list[str]=Field(description="list of campaign ideas with brief description")





class campaign(BaseModel):
    # Campaign Details
    name: str = Field(..., description="Name of the marketing campaign")
    description: str = Field(None, description="Brief description of the campaign")
    start_date: str = Field(..., description="Start date of the campaign (YYYY-MM-DD)")
    end_date: Optional[str] = Field(None, description="End date of the campaign (YYYY-MM-DD)")
    budget: float = Field(..., description="Allocated budget for the campaign in USD")

    # Goals
    goals: List[str] = Field(..., description="Goals of the campaign, e.g., 'Increase brand awareness', 'Generate leads'")

    # Target Audience
    audience_age_range: Optional[List[int]] = Field(None, description="Age range of the target audience, e.g., [18, 35]")
    audience_demographics: Optional[dict] = Field(None, description="Demographics of the target audience, e.g., {'location': 'USA', 'interests': ['fitness', 'technology']}")

    # Channels
    channels: List[str] = Field(..., description="Marketing channels used for the campaign, e.g., 'Social Media', 'Email', 'PPC'")
    primary_channel: Optional[str] = Field(None, description="The primary channel used for the campaign")

    # Content Details
    key_message: str = Field(..., description="The primary message of the campaign")
    assets: List[HttpUrl] = Field(..., description="List of URLs to campaign assets, e.g., images, videos, or documents")

    # Performance Metrics
    expected_roi: Optional[float] = Field(None, description="Expected return on investment for the campaign")
    kpis: Optional[List[str]] = Field(None, description="Key performance indicators, e.g., 'CTR', 'Conversion Rate'")
