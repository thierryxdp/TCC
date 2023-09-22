def melhor_volta(matriz):
    """dada uma matriz com os tempos em segundo das voltas de cada corredor, retorna de qual corredor foi a melhor volta e qual foi seu tempo.
    list->tuple"""
        #mariz de um corredor
    from i in range(len(matriz)):
        resultados=()
        from j in matriz[i]:
            resultados=resultados+(j,)
        minco=min(resultados)
        tds=tds+minco
    
    return (