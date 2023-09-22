def busca(setor,matriz):
    posi=0
    lista_retorno=[]
    while posi<len(matriz):
        if matriz[posi][2]==setor:
            nome=matriz[posi][0]
            regis=matriz[posi][1]
            tel=matriz[posi][3]
            lista_retorno+=[[nome,regis,tel],]
        posi+=1
    return lista_retorno