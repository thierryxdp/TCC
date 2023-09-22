def busca(setor,matriz):
    """
    Essa função recebe uma matriz e um setor, e retorna o contato 
    das pessoas que trabalham nesse setor de acordo com a matriz;
    str, list -> list
    """
    resultado = []
    for i in matriz:
        if setor in i:
            resultado.append(i)
    for x in resultado:
        list.pop(x, 2)
    return resultado