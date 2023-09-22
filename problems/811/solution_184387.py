def colchao(medidas,H,L):
    """Função que retorna se dar para passar o colchao na porta
       Parametros: list,int,int -> bool
       Use medidas: medidas do colchão ordenadas da menor para maior
       Use H: altura da porta
       Use L: largura da porta
       """
    a,b,c = medidas[0],medidas[1],medidas[2]
    menor_lado = min(a,b,c)
    lista_segundo_lado = []
    if menor_lado != a:
        lista_segundo_lado.append(a)
    elif menor_lado != b:
        lista_segundo_lado.append(b)
    else:
        lista_segundo_lado.append(c)
    segundo_menor = min(lista_segundo_lado)
    if menor_lado <= L and segundo_menor <= H:
        return True
    else:
        return False