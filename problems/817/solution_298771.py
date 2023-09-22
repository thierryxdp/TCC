def acima_da_media(notas):
    """retorna uma nova lista com as notas que ficaram acima da media da turma;
    list -> list"""
    
    media=sum(notas)/len(notas)
    
    list.append(notas,media)
    list.sort(notas)
    i=(list.index(notas,media))+1
    
    return notas[i:]