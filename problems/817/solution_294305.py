def acima_da_media(lista):
    " " "Calcula e retorna a de acordo com uma lista de notas(lista) as notas que ficaram acima da media; list, ->list " " "
    n = sum(lista)/len(lista)
    if n in lista:
        list.sort(lista)
        a = list.index(lista,n)
        return lista[a+1:]
    if n not in lista:
        list.append(lista,n)
        list.sort(lista)
        a = list.index(lista,n)
        return lista[a+1:]