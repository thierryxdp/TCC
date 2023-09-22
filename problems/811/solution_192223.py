def colchao(medidas,h,l):
    """Função que retorna um valor booleano pra saber se um colchão de medidas a,b,c passa por uma porta de medidas h,l.
    list,int,int -> bool
    Use medidas: Medidas do colchão em ordem crescente.
    Use h: Altura da portão
    Use l: Larguda da porta"""
    #Medidas do colchão
    a,b,c = medidas[0],medidas[1],medidas[2]
    #Encontrar o menor lado do colchão para o menor lado da porta
    primeiro_menor_lado_colchao = min(a,b,c)
    #Encontrar o segundo menor lado do colcão para o segundo menor lado da porta
    lista_segundo_lado_colchao = []
    if primeiro_menor_lado_colchao != a:
        lista_segundo_lado_colchao.append(a)
    elif primeiro_menor_lado_colchao != b:
        lista_segundo_lado_colchao.append(b)
    else:
        lista_segundo_lado_colchao.append(c)
    segundo_menor_lado_colchao = min(lista_segundo_lado_colchao)
    #Condição que vai comparar os lados do colchão com as medidas da porta.
    if primeiro_menor_lado_colchao <= l and segundo_menor_lado_colchao <= h:
        return True
    elif:
        return False
    else:
        return False