# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
 
def substitui(s:str,x:str,i:int)->str:
    '''Funcao que retorne uma string s, substituindo o elemento da 
    posicao i pelo caractere x'''
    return s[0:i]+x+s[i+1:]