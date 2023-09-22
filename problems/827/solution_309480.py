def qtd_divisores(numero):
    ''' Função que conta a quantidade de divisores do inteiro dado como entrada
    int -> int '''
    divisores = [numero]
    for ele in list(range(numero)):
        if numero<=0:
            return 0
        
        elif ele>0 and numero%ele == 0:
            list.append(divisores,ele)
            return len(divisores)