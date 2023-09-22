# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
import math
def hashtag(s):
    """recebe uma string e insere o caractere '#' no início,no meio e no final dela"""
    return str('#')+str(s)[0:math.floor((len(s)/2))]+str('#')+str(s)[math.floor(len(s)/2):]+str('#')