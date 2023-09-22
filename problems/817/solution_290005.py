def acima_da_media(notas):
    "função que dada uma lista com notas, retorna essa lista ordenada com as notas acima da média.list->list."
    soma = sum(notas)
    med = sum(notas)/len(notas)
    if med in notas:
        list.sort(notas)
        x = list.index(notas,med)
        return notas[x+1:]
    else:
        notas.append(med)
        list.sort(notas)
        y=list.index(notas,med)
        return notas[y+1:]