def busca(setor,matriz):
    """Funcao que busca funcionarios por setor;
    entrada: str,list
    saida:list"""
    
    lista=[]
    
    for linha in matriz:
        if linha[2] == setor:
            list.pop(linha,2)
            list.append(lista,linha)
    return lista