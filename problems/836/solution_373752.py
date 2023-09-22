def busca(setor,matriz):
    """retorna os dados de um funcionario de um determinado setor inscrito em uma matriz; str, list-> list"""
    contato=[]
    for i in matriz:
        if matriz[i][2]==setor:
            add=matriz[i][:2]+matriz[i][3:]
            list.append(contato,add)
    return contato