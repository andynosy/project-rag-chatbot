from fastapi import APIRouter

router = APIRouter()

@router.get("/available")
async def get_available_models():
    return {
        "models": [
            {"id": "gpt-4", "name": "GPT-4", "provider": "OpenAI"},
            {"id": "gpt-3.5-turbo", "name": "GPT-3.5", "provider": "OpenAI"},
            {"id": "claude-2", "name": "Claude 2", "provider": "Anthropic"},
            {"id": "claude-instant-1", "name": "Claude Instant", "provider": "Anthropic"}
        ]
    }