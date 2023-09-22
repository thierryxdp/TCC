def hashtag(s):
    """ funcao hashtag
    # str-> str """
    nova_string = '#' + s[:len(s)//2] + '#' + s[:len(s)//2] + '#'
    return nova_string