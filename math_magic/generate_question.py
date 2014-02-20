import json
import sympy

from replace_random_seeds import replace_random_seeds

def generate_question(user_input):
    '''
    return a json object containing the question formatted based on user_input
    '''
    data = {}
    data['user_input'] = user_input
    data['plain_text'] = replace_random_seeds(user_input)
    data['answer'] = 5

    return json.dumps(data)


