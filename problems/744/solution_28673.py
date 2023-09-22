# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    'função que recebe um texto e retorna a string com o caractere jogo da velha no inicio,meio e final dela, caso seja impar ira colocar no meio-1'
    if len(s)%2==0:
        metade_da_string=len(s)/2
        return '#'+s[0:int(metade_da_string)]+'#'+s[int(metade_da_string):]+'#'
    else:
        metade_da_string=len(s)/2-0.5
        return '#'+s[0:int(metade_da_string)]+'#'+s[int(metade_da_string):]+'#'