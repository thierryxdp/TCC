filtra_pares(tupla):
    """Essa função filtra os elementos pares da tupla.
    Como entrada temos uma tupla com quatro elementos, e como saída 
    temos uma tupla com os elementos pares;
    tuple->tuple"""
    numero_1= int(tupla[0])%2
    numero_2=int(tupla[1])%2
    numero_3=int(tupla[2])%2
    numero_4=int(tupla[3])%2
    if numero_1==0 and numero_2==0 and numero_3==0 and numero_4==0:
        return (numero_1,numero_2,numero_3,numero_4)
    elif numero_1==0 and numero_2==0 and numero_3==0 :
        return (numero_1,numero_2,numero_3)
    elif numero_1==0 and numero_2==0:
        return (numero_1,numero_2)
    elif numero_1==0:
        return (numero_1,)
    else:
        ()