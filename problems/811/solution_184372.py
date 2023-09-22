def colchao(medidas,h,l):
    """Função que retorna um valor booleano para saber se um colchão de medidas a, b e c passa pela porta de medidas h e l
       Parametros: list,int,int ->
       Use medidas: ordenada da menor para a maior
       Use h: altura da porta
       Use l: largura da porta"""
    a,b,c = medidas[0],medidas[1],medidas[2]
    menor_lado_colchao = min(a,b,c)
    lista_segundo_lado = []
    if menor_lado_colchao != a:
        lista_segundo_lado.append(a)
    elif menor_lado_colchao !=b:
        lista_segundo_lado.append(b)
    else:
        lista_segundo_lado.append(c)
    segundo_menor_lado = min(lista_segundo_lado)
    if menor_lado_colchao <= 1 and segundo_menor_lado <= h:
        return True
    else:
        False