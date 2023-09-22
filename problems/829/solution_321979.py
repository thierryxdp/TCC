def soma_h(numero):
    'dado um numero, fara a soma h= 1+1/2+1/3...1/numero'
    H=0
    lista_de_Ns=list(range(1,numero+1))
    for numero in lista_de_Ns:
        H+= 1/numero
    return round(H,2)