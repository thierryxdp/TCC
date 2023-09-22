'''
	A função pega string s e adiciona # no seu início, fim e 
    meio (no caso de len(s) for um número impar o # será
    adicionado de forma que fique um caracter a mais a 
    esquerda do # em relação a direita).
    s ->str
'''
# str-> str
def hashtag(s):
    return '#'+s[:(len(s)//2)]+'#'+s[(len(s)//2):]+'#'