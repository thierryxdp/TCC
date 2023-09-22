def busca (setor,matriz):
    """Função que retorna todos os dados dos funcionários do setor
    escolhido, na matriz de entrada.
    str,list->list"""
    funcionarios=[]
    for linha in matriz:
        for item in linha:
            if item==setor:
                linha.remove(setor)
                funcionarios+=[linha]
    return funcionarios