# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''Função que retorna uma string igual a s, porém substitui o elemento 
       da posição I pelo caractere X
       str, int, int -> str
       
       Parameters:
       s: String escolhida
       x: Caractere escolhido
       i: Número inteiro entre 0 e o comprimento da string.
       '''
    return s[0:i] + x + s[i+1:]