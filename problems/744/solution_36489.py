def hashtag(s):
    """funçao que recebe uma string e insere o caractere
    # no inicio, no meio e no final dela
    str-> str"""
    return '#' + s[0:int(len(s)/2)] + '#' + s[int(len(s)/2):] + '#'