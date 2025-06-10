from pydantic_settings import BaseSettings


class TeamSettings(BaseSettings):
    """Team settings that can be set using environment variables.

    Reference: https://pydantic-docs.helpmanual.io/usage/settings/
    """

    gpt_4_mini: str = "gpt-4o-mini"
    gpt_4: str = "gpt-4o"
    gpt_41_mini: str = "gpt-4.1-mini-2025-04-14"
    gpt_41: str = "gpt-4.1-2025-04-14"
    or_free_model: str = "google/gemini-2.5-flash-preview-05-20"
    embedding_model: str = "text-embedding-3-small"
    default_max_completion_tokens: int = 16000
    default_temperature: float = 0


# Create an TeamSettings object
team_settings = TeamSettings()
