def maiores(lista,n):
    lista.sort()
    if n in lista:
        ola = lista.index(n)
        nov = lista[ola:]
        return nov
    else:
        lista.append(n)
        lista.sort()
        ola= lista.index(n)
        nov = lista[ola:]
        nov.remove(n)
        return nov
def acima_da_media(lista,n=5):
    resp = maiores(lista,n)
    divisao = len(lista)/len(resp)
    if len(lista)>1:
        elif len(lista)> 5:
       		elif divisao != 2:
            	resp.remove(n)
           		return resp
    if len(lista)>1:
        resp = maiores(lista,n)
        return resp
    else:
        return[]