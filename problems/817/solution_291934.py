def acima_da_media(lista):
    """Dada uma lista com notas de alunos, retorna uma nova lista ordenada apenas com as notas que estao acima da media da turma"""
    """Entrada:lista
    saida:lista"""
    
    media = (sum(lista)//len(lista))
    
    if media in lista:
        
        list.sort(lista)
        x = list.index(lista,media)
        
        return lista[x+1:]
    
    else:
        
        list.append(lista,media)
        list.sort(lista)
        y = list.index(lista,media)
        
        return lista[y+1:]