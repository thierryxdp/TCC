def acima_da_media(lista_notas):
    '''
    	Funcao que recebe uma lista com as notas dos alunos 
        de uma turma e retorna uma lista ordenada com as 
        notas que ficaram acima da media
        list -> list
    '''
    media = sum(lista_notas)/len(lista_notas)
    return media