import sys, random


def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""

    chains = {}
    list_of_words = corpus.split()    

    for i in range(len(list_of_words)-2):
        word_tuple = (list_of_words[i], list_of_words[i +1])
        if chains.has_key(word_tuple):
            chains[word_tuple].append(list_of_words[i + 2])
        else:
            chains[word_tuple] = [list_of_words[i + 2]]
    return chains

def make_sentence(chain, chain2):
    chain_tuples = chain.keys()
    chain2_tuples = chain2.keys()

    #Make first three words
    cap_tuples = []
    for item in chain_tuples:
        if ord(item[0][0]) >= ord("A") and ord(item[0][0]) <= ord("Z"):
            cap_tuples.append(item)
    rand_tuple = cap_tuples[random.randint(0, len(cap_tuples)-1)]
    add_word = chain[rand_tuple][random.randint(0, len(chain[rand_tuple])-1)]
    second_word = rand_tuple[1]
    rand_string = rand_tuple[0] + " " + second_word + " " + add_word

    #Use last word for first chain, search in chain2's tuple list for start word
    possible_tuples = []
    for item in chain2_tuples:
        if item[0] == add_word:
            possible_tuples.append(item)

    #Cover edge case: no possible tuple matches in second text for add_word
    if len(possible_tuples) == 0:
        rand_tuple = cap_tuples[random.randint(0, len(cap_tuples)-1)]
        add_word = chain[rand_tuple][random.randint(0, len(chain[rand_tuple])-1)]
        second_word = rand_tuple[1]
        rand_string = rand_tuple[0] + " " + second_word + " " + add_word
    bridge_tuple = possible_tuples[random.randint(0, len(possible_tuples) - 1)]

    first_word = bridge_tuple[0]
    second_word = bridge_tuple[1]
    add_word = chain2[bridge_tuple][random.randint(0, len(chain2[bridge_tuple])-1)]
    rand_string += " " + bridge_tuple[1]
    
    i = 0
    while add_word[len(add_word)-1] not in "!.?":
        first_word = second_word
        second_word = add_word
        if i % 2 == 0:
            add_word = chain[(first_word, second_word)][random.randint(0, len(chain[(first_word, second_word)])-1)]
        else:
            add_word = chain2[(first_word, second_word)][random.randint(0, len(chain2[(first_word, second_word)])-1)]
        rand_string += " " + add_word 
        i += 1

    return rand_string

def main():
    script, textfile, textfile2 = sys.argv

    f = open(textfile)
    text = f.read().replace('"', ' ')
    f.close()

    f2 = open(textfile2)
    text2 = f2.read().replace('"', ' ')
    f2.close()

    text = make_chains(text)
    text2 = make_chains(text2)
    print make_sentence(text, text2)

if __name__ == "__main__":
    main()