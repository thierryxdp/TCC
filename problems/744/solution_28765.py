def hashtag(s):
    '''Função que, dada uma string qualquer, retorna essa string com a presença de 3 hashtags: uma no começo; outra no meio; e outra no final.
str --> str'''
    return '#' + str(s)[0:len(s)//2] + '#' + str(s)[len(s)//2:] + '#'