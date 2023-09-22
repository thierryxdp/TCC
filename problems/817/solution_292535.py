def maiores(lista, n):
    list(lista)
    lista.append(n)
    lista_nov = sorted(lista)
    indN = lista_nov.index(n)
    if n not in lista_nov:
        lista.append(n)

    return lista_nov[indN + 1:]

def acima_da_media(lista):
    """Funçao que dada uma lista de notas de um aluno calcula a sua média e retorna os alunos notas que estão
    acima da média."""
    media = sum(lista)/(len(lista))
    alunosaprovados = maiores(lista, media)
    return alunosaprovados