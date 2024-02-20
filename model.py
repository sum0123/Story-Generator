import random


def make_markov_model(cleaned_stories, n_gram=3):
    markov_model = {}

    for i in range(len(cleaned_stories) - n_gram - 1):
        curr_state, next_state = "", ""
        for j in range(n_gram):
            curr_state += cleaned_stories[i + j] + " "
            next_state += cleaned_stories[i + j + n_gram] + " "
        curr_state = curr_state[:-1]
        next_state = next_state[:-1]
        if curr_state not in markov_model:
            markov_model[curr_state] = {}
            markov_model[curr_state][next_state] = 1
        else:
            if next_state in markov_model[curr_state]:
                markov_model[curr_state][next_state] += 1
            else:
                markov_model[curr_state][next_state] = 1

    # calculating transition probabilities
    for curr_state, transition in markov_model.items():
        total = sum(transition.values())
        for state, count in transition.items():
            markov_model[curr_state][state] = count / total
    
    return markov_model


# def generate_story(markov_model, limit, start):
#     n = 0
#     curr_state = start
#     next_state = None
#     story = ""
#     story += curr_state + " "
#     while n < limit:
#         next_state = random.choices(
#             list(markov_model[curr_state].keys()),
#             list(markov_model[curr_state].values()),
#         )

#         curr_state = next_state[0]
#         story += curr_state + " "
#         n += 1
#     return story
