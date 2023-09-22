def acima_da_media(nota):
    """Funcao que dada uma lista de entrada com as notas dos alunos
    de uma turma retorna uma lista ordenada com as notas acima da 
    media da turma;list->list"""
	media = sum(nota)/len(nota)
    resultado = maiores(nota,media)	
    if resultado[0] == media:
        del resultado[0]   
    return resultado
def maiores(lista,n):
    lista.append(n)
    lista.sort()
    lista.index(n)  
    indice_lista = lista.index(n)
    
    return lista[indice_lista+1:]