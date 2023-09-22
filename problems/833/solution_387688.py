def conta_numero(numero,matriz):
    '''função que dado um numero int e uma matriz retorna qua
    ntas vezes numero aparece matriz;int,list->int'''
    resp=[]
    for i in matriz:
        for j in i:
            if numero == j:
                list.append(resp,numero)
    return len(resp)