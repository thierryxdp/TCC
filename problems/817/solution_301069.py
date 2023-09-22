def acima_da_media(lista,n=5):
    resp = maiores(lista,n)
    divisao = len(lista)/len(resp)
    if len(lista)>1:
        if divisao != 2:
            resp.remove(n)
            return resp
    if len(lista)>1:
        resp = maiores(lista,n)
        return resp
    else:
        return[]