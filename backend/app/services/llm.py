from langchain.chat_models import ChatOpenAI, ChatAnthropic
from langchain.schema import SystemMessage, HumanMessage
from ..core.config import settings

class LLMService:
    def __init__(self, model_name: str = "gpt-4"):
        self.model_name = model_name
        if model_name.startswith("gpt"):
            self.llm = ChatOpenAI(
                model_name=model_name,
                openai_api_key=settings.OPENAI_API_KEY,
                temperature=0
            )
        elif model_name.startswith("claude"):
            self.llm = ChatAnthropic(
                model=model_name,
                anthropic_api_key=settings.ANTHROPIC_API_KEY,
                temperature=0
            )

    def generate_response(self, query: str, context: str) -> str:
        messages = [
            SystemMessage(content="You are a helpful assistant. Use the provided context to answer questions accurately. If you're unsure or the context doesn't contain the answer, say so."),
            HumanMessage(content=f"Context: {context}\n\nQuestion: {query}")
        ]
        
        response = self.llm.generate([messages])
        return response.generations[0][0].text