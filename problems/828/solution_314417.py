def primo(numero):
    'funcao que dado um numero, retorna True se for primo e False se não for primo'
    primo=True
    n_primo=False
    lista_de_possiveis_divisores=list(range(1,int((numero/2))+1))
    lista_de_divisores=[]
    if numero ==1:
        return primo
    for divisor in lista_de_possiveis_divisores:
        if numero%divisor==0:
            list.append(lista_de_divisores,divisor)
    if len(lista_de_divisores) ==1:
        return primo
    else:
        return n_primo