def acima_da_media(lista):
    """Função que dada uma lista(lista) com as notas dos alunos da turma,
    retorne uma lista ordenada com as notas que ficaram acima da média.
    lista -> lista"""
    
    media = int(sum(lista)/len(lista))+1
    if(media in lista):
        list.sort(lista)
        a = lista[(list.index(lista,media)):] 
    else:
        lista[0:0] = [media]
        list.sort(lista)
        a = lista[(list.index(lista,media))+1:]
    return a