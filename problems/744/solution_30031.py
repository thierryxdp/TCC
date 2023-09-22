def hashtag(s):
    '''funcao que recebe uma string e devolve ela com o caractere # no inicio,meio e fim;
    string-> string '''
    divisao= len(s)//2
    return '#'+str(s)[0:divisao]+'#'+str(s)[divisao:]+'#'