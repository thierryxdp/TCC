def busca(setor,matriz):
    "Função que ao receber uma matriz e uma palavra chave, retorna as informações armazenadas na matriz que compreendem a palavra chave. str, list --> tuple"
    lista=[]
    for i in range(len(matriz)):
        if setor in matriz[i]:
    		lista=lista+[[matriz[i][0],matriz[i][1],matriz[i][3]]]
    return lista