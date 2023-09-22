def media(lista):
    """retorne a média da turma e uma lista ordenada com as notas que
    ficaram acima da média; list => list"""
    
    acima_media = []
    m = sum(lista)
    m = m / len(lista)

    for i in lista:
        if(i > m):
            acima_media.append(i)
    
    acima_media.sort()
    
    return m, acima_media