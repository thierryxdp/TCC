def busca(setor,matriz):
    """Retorna os funcionarios a prtir do setor determinado;
    	str,list -> list"""
    func = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == setor:
                func = func + [matriz[i]]
    i = 0
    while i < len(func):
        func[i].remove(setor)
        i = i+1
    return func