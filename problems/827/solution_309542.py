def qtd_divisores(n):
    '''função que dado um numero(n), retorna quantos divisores
    n tem;int->int'''
    divisor=1
    indice=0
    resp=[]
    for i in range((n-1),(n+1)):
        if (n%divisor)== 0:
            resp+=(list.insert(resp,indice,str(n%divisor)))
        divisor+=1
        indice+=1
    return len(resp)