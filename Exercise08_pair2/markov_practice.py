import random

def make_sentence(chain, chain2):
    chain_tuples = chain.keys()
    chain2_tuples = chain2.keys()

    #Make first three words
    cap_tuples = []
    for item in chain_tuples:
        if ord(item[0][0]) >= ord("A") and ord(item[0][0]) <= ord("Z"):
            cap_tuples.append(item)
    rand_tuple = cap_tuples[random.randint(0, len(cap_tuples)-1)]
    add_word = chain_tuples[rand_tuple][random.randint(0, len(chain_tuples[rand_tuple])-1)]
    second_word = rand_tuple[1]
    rand_string = rand_tuple[0] + " " + second_word + " " + add_word

    #Use last word for first chain, search in chain2's tuple list for start word
    possible_tuples = []
    for item in chain2_tuples:
        if item[0] == add_word:
            possible_tuples.append(item)

    i = 0
    while add_word[len(add_word)-1] not in "!.?":
        first_word = second_word
        second_word = add_word
        if i % 2 != 0:
            add_word = chain2_tuples[(first_word, second_word)][random.randint(0, len(chain2_tuples[(first_word, second_word)])-1)]
        else:
            add_word = chain_tuples[(first_word, second_word)][random.randint(0, len(chain_tuples[(first_word, second_word)])-1)]
        rand_string += " " + add_word 
        i += 1

    return rand_string