# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
from math import ceil
def hashtag(s):
    '''faz com que # seja posto no inicio, meio e fim 
    de uma string ex: #ab#cd#'''
    primeiraParteString=s[0:(len(s)//2)]
    segundaParteString=s[ceil(len(s)/2):len(s)]
    return '#'+primeiraParteString+'#'+segundaParteString+'#'