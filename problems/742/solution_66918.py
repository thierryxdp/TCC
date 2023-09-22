# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """ dados uma str s, um caractere x e um int i entre 
    0 e comprimento da str, retorna uma str parecida com s 
    mas no lugar da posicao i sera substituido pelo
    caractere x
    str, str, int -> str"""
    palavra = s
    inicio_de_palavra = palavra[0:i]
    fim_de_palavra = palavra[1+i:]
    return inicio_de_palavra + x + fim_de_palavra