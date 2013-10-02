import sys, random, twitter


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

def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""

    list_of_tuples = chains.keys()
    
    # cap_tuples = []
    # for item in list_of_tuples:
    #     if ord(item[0][0]) >= ord("A") and ord(item[0][0]) <= ord("Z"):
    #         cap_tuples.append(item)

    #Creates first two words of sentence
    rand_tuple = list_of_tuples[random.randint(0, len(list_of_tuples)-1)]
    add_word = chains[rand_tuple][random.randint(0, len(chains[rand_tuple])-1)]
    second_word = rand_tuple[1]
    rand_string = rand_tuple[0] + " " + second_word + " " + add_word

    #Creates the middle and last word of sentence
    while add_word[len(add_word)-1] not in "!.?":
        first_word = second_word
        second_word = add_word
        add_word = chains[(first_word, second_word)][random.randint(0, len(chains[(first_word, second_word)])-1)]
        rand_string += " " + add_word


    return rand_string

def main():
    # api = twitter.Api(
    #     consumer_key= 'RhrXe9gLhQBO41140HA',
    #     consumer_secret= 'WBmD6NqJEgcC15sKCewEI3zPX2mMpVvtDhK3sSR0sQ', 
    #     access_token_key='1925137250-wJPM9pnev0zKGKMIVMq7H1scqXzBEK1RX3e9skC', 
    #     access_token_secret='mKKY2wfQVnFVVYCfMUjmh03dRwH51Ylg0wSS4rzehSU'
    #     )
    script, textfile = sys.argv

    f = open(textfile)
    text = f.read().replace('"', '')
    text_lower = text.lower()
    f.close()
    
    # while True:
    #     status = api.PostUpdate(make_text(make_chains(text)))
    #     if len(status.text) <= 140:
    #         break

    # print status.text

    print make_text(make_chains(text_lower))


main()