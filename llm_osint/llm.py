from langchain.chat_models import ChatOpenAI
from langchain.chat_models.base import BaseChatModel
from langchain_deepseek import ChatDeepSeek

LLMModel = BaseChatModel

default_fast_llm_options = dict(model_name="deepseek-chat", request_timeout=120, max_retries=10, temperature=0.7)
default_llm_options = dict(model_name="deepseek-chat", request_timeout=120, max_retries=10, temperature=0.7)


def get_default_fast_llm() -> LLMModel:
    chat = ChatDeepSeek(**default_fast_llm_options)
    return chat


def get_default_llm() -> LLMModel:
    chat = ChatDeepSeek(**default_llm_options)
    return chat
