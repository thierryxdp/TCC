def busca(setor,matriz):
    """Retorna os contatos dos funcionarios do setor
    str,list-->list"""
    ret=[]
    for linha in matriz:
        for coisa in linha:
            if coisa == setor:
                list.remove(linha,setor)
                list.append(ret,linha)
    return ret