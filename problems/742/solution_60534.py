# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):

    lista = list(s)
    tam = len(s)
    for j in range(tam):
      if j == i:
        lista[j]=x

    s = ''.join(lista)
    return s