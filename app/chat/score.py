from app.chat.redis import client
import random

def random_component_by_score(component_type, component_map):
    #make sure component_type is llm, retrievery or memory
    if component_type not in ["llm", "retriever", "memory"]:
        raise ValueError("Invalid component_type")
    #from reddis, get the sum of total scores for the given type
    values = client.hgetall(f"{component_type}_score_values")
    #from redis, get the hash containing the number of times each component has been voted on
    counts = client.hgetall(f"{component_type}_score_counts")
    #gell all the valid component names from the component map
    names = component_map.keys()
    #Loop over those valid names and use them to calculate the average score
    #Add the average score to the dictionary
    avg_scores = {}
    for name in names:
        score = int(values.get(name, 1))
        count = int(counts.get(name, 1))
        avg = score / count
        avg_scores[name] = max(avg, 0.1)
    #Do a weighten random selection
    sum_scores = sum(avg_scores.values())
    random_val = random.uniform(0, sum_scores)
    cumulative = 0

    for name, score in avg_scores.items():
        cumulative += score
        if random_val <= cumulative:
            return name
    
    
    
def score_conversation(
    conversation_id: str, score: float, llm: str, retriever: str, memory: str
) -> None:
    score = min(max(score, 0), 1)

    client.hincrby("llm_score_values", llm, score)
    client.hincrby("llm_score_counts", llm, 1)
    
    client.hincrby("retriever_score_values", retriever, score)
    client.hincrby("retriever_score_counts", retriever, 1)
    
    client.hincrby("memory_score_values", llm, score)
    client.hincrby("memory_score_counts", llm, 1)
    



def get_scores():
    """
    Retrieves and organizes scores from the langfuse client for different component types and names.
    The scores are categorized and aggregated in a nested dictionary format where the outer key represents
    the component type and the inner key represents the component name, with each score listed in an array.

    The function accesses the langfuse client's score endpoint to obtain scores.
    If the score name cannot be parsed into JSON, it is skipped.

    :return: A dictionary organized by component type and name, containing arrays of scores.

    Example:

        {
            'llm': {
                'chatopenai-3.5-turbo': [score1, score2],
                'chatopenai-4': [score3, score4]
            },
            'retriever': { 'pinecone_store': [score5, score6] },
            'memory': { 'persist_memory': [score7, score8] }
        }
    """

    pass
