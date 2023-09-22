def acima_da_media(lista):
    ''' Calcular uma funcao que dada as notas dos alunos, retorne outra lista com as notas acima da media;
    list -> list'''
    
    list.sort(lista)
   
    media = (sum(lista))/len(lista)
    
    return lista[media:]