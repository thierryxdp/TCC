def colchao(medidas,H,L): 
    """funcao que calcula se o colchao escolhido passa pela porta
       dadas as suas medidas (em ordem crescente) e as dimencoes da 
       porta tais que H=altura e L=largura
       
       OBS: insira todos os parametros em centimetros 
       
       lista,int,int-> str
       
    """
    lista_medidas= list(medidas)
    
    h=lista_medidas[0]
    l=lista_medidas[1]
    c=lista_medidas[2]
    
    if c>H and l<H and h<L:
        return "True"
    
    elif c<H and l>H and h<L:
        return "True"

    elif c<H and L<H and h<L:
        return "True"
    
    elif c>H and l>H:
        return "False"
    
    else:
        return "False"