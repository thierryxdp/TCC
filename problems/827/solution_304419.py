def qtd_divisores(n):
    lista=[1]
    aux=0
    from math import ceil
    if n==1:
        return 
    else:
        if n==2:
            return
        else:
            for x in range(2,ceil(n**(1/2))+1,1):
                if n%x==0:
                    lista.append(x)
                    aux=aux+1
            if aux==0:
                return str(n)
            else:
                for x in range(ceil(n**(1/2))+1,n+1,1):
                    if n%x==0:
                        lista.append(x)
                        aux=aux+1
                return str.format(aux+1, lista)