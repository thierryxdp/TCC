#Questão4
def maiores(lista, n):
    '''Função que retorna uma lista ordenada com os números maiores que n fornecidos'''
    '''list, int -> list'''
    list.insert(lista,0,n)
    list.sort(lista)
    local_De_n = list.index(lista,n)
    nobalist = lista[local_De_n+1:]
    return nobalist

#Questão5
def acima_da_media(notas):
    '''função que retorna uma lista com as notas acima da média calculadas entre elas mesmas'''
    media = sum(notas)/len(notas)
    return maiores(notas, media)