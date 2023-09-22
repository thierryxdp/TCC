def acima_da_media(lista):
    '''
    Função que dada uma lista com notas do alunos, retorna uma lista ordenada das notas acima da média
    list -> list
    ''''
    def maiores(lista,n):
        list.append(lista,n)
        list.sort(lista)
        nyx=list.index(lista,n)
        return lista[nyx+1:]
    media=sum(lista)/len(lista)
    if(media in lista):
        d=maiores(lista,media)
        return d[1:]
    else:return maiores(lista,media)