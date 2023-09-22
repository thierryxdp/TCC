def colchao(medidas,H,L):
    '''Função que dadas as medidas do colchão, analisa se o mesmo passará na porta com as medidas de H e L também dadas como variáveis.
    
    lista,int,int -> string
    lista,float,int -> string
    lista,float,float -> string
    lista,int,float -> string'''

    if medidas[1]>H:
        return "False"
    else:
        return "True"