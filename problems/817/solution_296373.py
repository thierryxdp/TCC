def acima_da_media(lista):
    '''Função que, dada uma lista com as notas dos alunos de uma turma
    	retorna uma lista com as notas ordenadas apenas dos que ficaram
        acima da média
        
        list -> list
        '''
    media=(sum(lista))//len(lista)
    if media in lista:
        list.sort(lista)
        list.reverse(lista)
        x=lista[0:list.index(lista,media)]
        return list.reverse(x)
    if media not in lista:
        lista = lista + [media]
        list.sort(lista)
        return lista[list.index(lista,media)+1:len(lista)]