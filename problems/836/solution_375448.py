def busca(setor,matriz):
    """Essa funcao recebe uma matriz e setores da empresa, e retorna o contato presente na matriz  
    str , list -> list"""
    resultado_busca = []
    for i in range (len(matriz)):
        if setor in matriz[i]:
            matriz[i].pop(2)
            resultado_busca.append(matriz[i])
    return resultado_busca