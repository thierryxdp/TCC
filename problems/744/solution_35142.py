def hashtag(s): 
    '''função que adiciona # no inicio no meio e no final das frases
    str-> str'''
    meio = len(s)//2
    return '#' + s [:meio] + '#' + s [meio+1:] + '#'