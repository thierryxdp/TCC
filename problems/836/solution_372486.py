def busca(setor,matriz):
    """Recebe uma matriz de dados de funcionários e um setor da empresa, retorna os dados de cada
    funcionário do setor; str, list -> list"""
    contador = 0
    resultado = []
    while contador < len(matriz):
        func = matriz[contador]
        if func[2] == setor:
            func = func[0:2]func[3]
            resultado.append(func)
        contador += 1
    return resultado