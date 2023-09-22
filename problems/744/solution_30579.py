def hashtag(s):
    '''
    Função que recebe uma string e devolve ela com hashtag no início,
    meio e fim;
    str -> str
    '''
    metade = int(len(s)/2)
    
    return '#' + str(s)[0:metade] + '#' + str(s)[metade:] + '#'