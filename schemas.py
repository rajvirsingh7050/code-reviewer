from pydantic import BaseModel, Field
from typing import List, Literal

class InlineComment(BaseModel):
    file_path: str = Field(description="Target file path under review")
    line_start: int = Field(description="Start line number of the code change")
    line_end: int = Field(description="End line number of the code change")
    severity: Literal["CRITICAL", "WARNING", "NITPICK"] = Field(description="Severity level")
    category: Literal["SECURITY", "PERFORMANCE", "LOGIC"] = Field(description="Issue category")
    issue_description: str = Field(description="Clear explanation of the flaw or bottleneck")
    suggested_code: str = Field(description="Exact replacement code for the GitHub suggestion block")

class PRReviewOutput(BaseModel):
    summary: str = Field(description="2-sentence executive summary of the review")
    comments: List[InlineComment] = Field(description="List of inline code suggestions")