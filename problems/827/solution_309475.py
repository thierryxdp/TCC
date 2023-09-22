def qtd_divisores(numero):
    ''' Função que conta a quantidade de divisores do inteiro dado como entrada
    int -> int '''
    divisores = [numero]
    antecessores_numero = list(range(numero))
    antecessores_fora0 = list.remove(antecessores_numero,[0])
    for ele in antecessores_fora0:
        if numero%ele == 0:
            list.append(divisores,ele)
    return len(divisores)