def maiores(lista,n):
    '''Essa função recebe lista e número inteiro e retorna
    lista com elementos da entrada a partir do número inteiro.
    list,int-->list'''
    if n in lista:
       list.sor(lista)
       lista1 =lista[list.index(lista,n) +1:]
       return lista1
    else:
       lista.insert(-1,n)
       list.sor(lista)
       lista1 =lista[list.index(lista,n) +1:] 
       return lista1
     
def acima_da_media(lista):
  ''' Função recebe lista e retorna lista ordena.list -->list'''
  media =int(sun(lista)/len(lista))
    return maiores(lista,media)