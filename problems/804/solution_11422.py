def filtra_pares(tupla):
    '''Função que retorna  todos os pares da tupla,
    sendo eles positivos ou negativos,entrada=int,int,int,int
    saida=int,int,int,int'''
    
    var_auxiliar = ()
    if tupla[0] % 2 == 0:
        var_auxiliar = var_auxiliar + (tupla[0],)
    if tupla[1] % 2 == 0:
        var_auxiliar = var_auxiliar + (tupla[1],)
    if tupla[2] % 2 == 0:
        var_auxiliar = var_auxiliar + (tupla[2],)
    if tupla[3] % 2 == 0:
        var_auxiliar = var_auxiliar + (tupla[3],)

    return var_auxiliar