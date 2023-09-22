def acima_da_media (lista_inteiros,n):
    '''função que recebe uma lista de números e retorna uma nota que recebe uma lista ordenada com as notas acima da media'''
list.insert (lista_inteiros,0,n)
list.sort (lista_inteiros,reverse=True)
x=list.index (lista_inteiros,n,0)
del lista_inteiros [x::-1]

return lista_inteiros [::-1]

def acima_da_media (notas):
    media notas= sum(notas)/len(notas)