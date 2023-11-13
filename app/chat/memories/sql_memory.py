from langchain.memory import ConversationBufferMemory
from app.chat.memories.histories.sql_history import SqlMessageHistory


from app.web.api import (
    get_messages_by_conversation_id,
    add_message_to_conversation
)

    
def build_memory(chat_args):
    return ConversationBufferMemory(
        chat_memory=SqlMessageHistory(
            conversation_id=chat_args.conversation_id
        ),
        return_messages=True,
        memory_key="chat_history",
        output_key="answer"
    )