def bolos(A, B, C):
    '''A função bolos aceita 3 parâmetros, que representam as
    	quantidades de: xícaras de farinha, ovos e colheres de sopa
        de leite disponíveis, nesta ordem. Tais parâmetros podem ser
        não inteiros. Dados estes parâmetros, a função retorna a variável
        quantidade, que representa quantos bolos podem ser feitos de
        acordo com a receita de bolo disponibilizada. Tal valor é sempre inteiro,
        dadas as limitações de João.
    A receita:
	
    A- 2 xícaras de farinha
    B- 3 ovos
    C- 5 colheres de sopa de leite
    
    A quantidade de bolos que ele pode fazer vai ser determinada
    pela quantidade de bolos que ele consegue fazer com o ingrediente limitante.
    Nesse caso, o ingrediente limitante vai ser aquele com o menor resultado da 
    divisão 
    	Quantidade deste ingrediente disponivel / Quantidade necessária
    
    Como João não é bom na cozinha, ele somente vai fazer números 
    inteiros de bolos:'''
    qnt_pela_xicara = A // 2
    qnt_pelo_ovo = B // 3
    qnt_pela_sopa = C // 5
    
    quantidade = min(qnt_pela_xicara, qnt_pelo_ovo, qnt_pela_sopa)
    return quantidade