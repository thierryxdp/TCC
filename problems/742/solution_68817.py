# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """ Essa função após receber os seguintes tres argumentos: uma string, um caractere qualquer,
    um numero inteiro entre 0 e o comprimento da string dada como argumento.
    Irá retronar uma string igual a dada como argumento porem,com o caractere dado na posição que tambem foi dada como argumentos.
    str, str, int -> str
    """
    a = s [:(i):]
   
    b = s [(i+1)::]       
   
    c = x
    
    return a + c + b