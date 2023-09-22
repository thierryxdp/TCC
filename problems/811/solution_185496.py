def colchao(medidas,H,L):
    """Funcao cujos parametros de entrada sao uma lista,
    chamada medida,com as dimensoes A,B e C do colchao que 
    Joao quer comprar, em centimetros, ordenadas da menor
    dimensao para a maior dimensao, e dois inteiros H e L,
    correspondentes, respectivamente, a altura e a largura
    das portas da casa de Joao, em centimetros. A funcao 
    retorna True, caso o colchao passe pelas portas e False,
    caso contrario;
    lista,int,int->bool"""
    
    x1=medidas[0]
    x2=medidas[1]
    
    if (x1<H and x2<L) or (x1<L and x2<H):
        return True
    else:
        return False