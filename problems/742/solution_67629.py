# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Retorna uma string igual a s, substituindo o elemento da posição i pelo caractere x. Entrada -> str, Saída -> str"""
    return str(s)[0:i] + str(x)+ str(s)[i+1:]