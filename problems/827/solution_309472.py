def qtd_divisores(numero):
    ''' Função que conta a quantidade de divisores do inteiro dado como entrada
    int -> int '''
    divisores = [numero]
    antecessores_numero = list(range(numero))
    for ele in list.remove(antecessores_numero,[0]):
        if numero%ele == 0:
            list.append(divisores,ele)
    return len(divisores)