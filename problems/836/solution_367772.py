def busca(setor,matriz):
    """Funcao que busca funcionarios por setor;
    entrada: str,list
    saida:list"""
    
    lista=[]
    
    for linha in matriz:
        if linha[2] == setor:
            list.append(lista,linha)
    return lista