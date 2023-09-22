def busca(setor,matriz):
    """Busca todos os contatos integrantes do setor dado,
    dentro de uma matriz dada;
    str, list -> list"""
    
    dados = []
    
    for x in matriz : 
        if setor in x : 
            list.append(dados,[x[0],x[1],x[3]])
                               
    return dados