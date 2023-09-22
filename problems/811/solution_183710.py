def colchao(medidas,H,L):
    """recebe as medidas do colchão,a altura e largura de sua casa e retorna 'True' caso o colchão possa passar pela porta e 'False' caso ocorra o contrário;list,int,int->Bool"""
    a=int(medidas[0])
    b=int(medidas[1])
    c=int(medidas[2])
    if int(a)=<int(H) and int(b)=<int(L) :
        return 'True'
    elif int(a)=<int(L) and int(b)=<int(H) :
        return 'True'
    else:
        return 'False'