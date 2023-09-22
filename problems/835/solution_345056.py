def melhor_volta(matriz):
    """Essa função retorna uma tupla com o melhor corredor, o seu melhor tempo
    e o número da volta com o melhor tempo. Como entrada uma lista e como saída
    uma tupla com todas as informações;
    list->tuple"""
    tupl_retorno=(0,3600,0)# utilizei essa tupla como referencia e acumulacao(o 3600 é um valor qualquer que não será antigido nunca sendo maior que qualquer número)
    for i in range(6):
        for j in range(10):
            if matriz[i][j]<tupl_retorno[1]:
                tupl_retorno = (i+1,matriz[i][j],j+1)
    return tupl_retorno