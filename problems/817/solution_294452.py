def acima_da_media(nota):
    """Dada uma lista com as notas dos alunos, retorna uma lista
    ordenada com as notas que ficaram acima da média;
    list -> list"""
    a = len(nota)
    b = sum(nota) 
    media = int(b/a)
    list.extend(nota,[media])
    list.sort(nota)
    y = list.index(nota,media)
    
    return nota[y+1:]