def acima_da_media(lista):
    '''funcao que recebe uma lista com notas de alunos e 
       retorna uma lista ordenada com os alunos que tiveram
       notas acima da media, utilizando a funcao da questao 
       anteior para ajudar a resolver e a funcao 'sum'
       list -> list'''
    def maiores(lista,n):
        list.append(lista,n)
        list.sort(lista)
        a=list.index(lista,n)
        return lista[a+1:]
    media=sum(lista)/len(lista)
    if(media in lista):
        d=maiores(lista,media)
        return d[1:]
    else:
        return maiores(lista,media)