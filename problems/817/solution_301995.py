def maiores(lista,n):
    '''A função retorna uma lista com todos os números da primeira
    que sejam maiores que n, ordenada em ordem crescente.
   	Assinatura: list,int->list'''
    lista_n= []
    for x in lista:
        if x>n:
            lista_n.append(x)
    lista_n.sort()
    return lista_n
def acima_da_media(lista):
     n=sum(lista)/len(lista)
        return n