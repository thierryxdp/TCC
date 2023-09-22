def acima_da_media(lista):
    """essa funçao recebe uma lista com notas de alunos e retorna, em ordem crescente, aquelas acima da media"""
    """entrada: list"""
    """saida: list"""
    m=(sum(lista)/len(lista))
    list.append(lista,m)
    list.sort(lista)
    if len(lista)==0:
        return []
    else:
    	return lista[((lista.index(m))+1):]