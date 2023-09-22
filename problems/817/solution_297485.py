def insere(lista_numero,n):
    'dada uma lista em ordem rescente, adiciona n de forma a manter a ordem, lista, int -> lista'
    return sorted(lista_numero + [n])
def maiores(lista_int,n):
    'Dada uma lista de inteiros e um inteiro n, retorna uma lista com todos os numeros maiores que n em ordem cresc. lista, int -> lista'
    lista_n = insere(lista_int,n)
    posicaoden = list.index(lista_n,n)
    return lista_n[posicaoden-:]
def acima_da_media(notas):
    'dada uma lista de notas, retorna as notas que ficaram acima da media. list -> list'
    media = sum(notas)/len(notas)
    return maiores(notas,media)