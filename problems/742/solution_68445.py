# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''
    Retorna uma string igual a "s", substituindo o elemento da posição "i" pelo caractere "x"
  	s=str.
    x=caractere.
    i=int. -> (entre 0 e o comprimento da string)
    
    '''
    l = list(s)
    l[i] = x
    new_s = "".join(l)
    return new_s