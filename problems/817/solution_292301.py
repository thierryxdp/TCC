def acima_da_media(lista_notas):
    """Calcula uma funcao que dada uma lista com as notas de uma turma,
    retorne uma lista ordenada com as notas que ficaram acima da media."""
    m=sum(lista_notas)/len(lista_notas)
    if m in lista_notas:
        list.sort(lista_notas)
        a=list.index(lista_notas,m)
        list.remove(lista_notas,m)
        return lista_notas[a:]
    if m not in lista_notas:
        list.append(lista_notas,m)
        list.sort(lista_notas)
        a=list.index(lista_notas,m)
        list.remove(lista_notas,m)
        return lista_notas[a:]