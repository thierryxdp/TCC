# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """função que recebe uma str (s), um caractere (x) e um numero inteiro (i)
    entre 0 e o comprimento de str (s), e retorna uma str igual a s exceto que o 
    elemento da posição i tenha que ser substituido por x 
    str, str, int --> str """
    sub_s1 = s [0:i] 
    sub = str.replace(sub_s1,i,x)
    return  sub