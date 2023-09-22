def acima_da_media(notas):
    """Função que irá receber uma lista com as notas dos alunos de uma turma e irá retornar uma lista com as notas que ficaram acima da média.
    	list -> list
        
    	Parameters:
        notas: lista com as notas dos alunos
        
        Returns:
        lista ordenada com as notas que ficaram acima da média
    """
    
    media = sum(notas)/len(notas)
    if media in notas:
        list.sort(notas)
        index = list.index(notas, media)
        return notas[index+1:]
    
    list.append(notas, media)
    list.sort(notas)
    index = list.index(notas,media)
	return notas[index+1:]