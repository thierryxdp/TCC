def acima_da_media(notas):
    """funcao que recebe como entrada uma lista com notas, faz a media 
    das notas, poe em ordem crescente e retorna somente as notas 
    acima da media.
    list->  list"""
    x = sum(notas)
    y = len(notas)
    z= int(x/y)

    if z in notas:
        a= notas
        list.sort(a)
        c= list.index(a,z)
        return a[c+1:]
    else: a= notas +[z]
    list.sort(a)
    c= list.index(a,z)
    return a[c+1:]