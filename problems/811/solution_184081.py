def colchao(medidas,h,l):
    '''Funcao que retorna um valor booleano pra saber se um colchao de medidas a,b,c passa por uma porta de medidas h,l;
    list,int,int -> bool''' 
    a,b,c = medidas[0],medidas[1],medidas[2]
    primeiro_menor_lado_colchao = min(a,b,c)
    lista_segundo_lado_colchao = []
    if primeiro_menor_lado_colchao != a:
        lista_segundo_lado_colchao.append(a)
    elif primeiro_menor_lado_colchao != b:
        lista_segundo_lado_colchao.append(b)
    else:
        lista_segundo_lado_colchao.append(c)
    segundo_menor_lado_colchao = min(lista_segundo_lado_colchao)
    if primeiro_menor_lado_colchao <= l and segundo_menor_lado_colchao <= h:
        return True
    else:
        return False