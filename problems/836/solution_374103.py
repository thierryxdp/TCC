def busca(setor,m):
    """Essa função busca todos os funcionarios de um setor
    str,lista->lista"""
    
    lista = []
    
    for i in range(len(m)):
        if setor == m[i][2]:
            lista = lista+[m[i]]
    
    
    
    return lista