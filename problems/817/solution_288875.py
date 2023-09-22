def maiores(lista, numero):
    """Dada uma lista e um número, está função retorna uma nova lista com todos os elementos
    da primeira lista que sejam maiores do que um determinado número.
       Onde: "lista" - lista inicial com diversos números;
             "numero" - número que servirá de parametro.
    list, int -> list"""
    lista.append(numero)
    lista.sort()
    indice = lista.index(numero)
    teste = lista.count(numero)
    if lista.count(numero) == teste:
        return lista[indice + teste:]


def acima_da_media(notas):
    """Função que informa as notas dos alunos que ficaram acima da média da turma.
       Onde: "notas" - é uma lista com a nota de todos os alunos da turma.
    list -> list """
    media  = sum(notas) / len(notas)
    notas_acima_media = maiores(notas, media)
    return notas_acima_media