# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
import math
def hashtag(s): 
    """insere # no inicio,meio e final da palavra dada como entrada"""
   return s[0:(math.floor(len(s)/2))]+ # +s[(math.floor(len(s)/2)):]+