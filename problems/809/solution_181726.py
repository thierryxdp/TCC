def intercala(lista1, lista2):
    '''Essa função, dada duas listas 1 2, retorna uma nova lista intercalando os elementos das listas 1 e 2, list,list -> list'''
    lista=[]
    for i in lista1 + lista2:
          lista.append(i)
          return list(lista)