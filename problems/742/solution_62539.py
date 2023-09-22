# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Retorna uma string s, substituindo o elemento da posição i pelo caractere x"""
    str.replace(i,x,1)
    return (s+str(i)+str(x))