def busca(setor,mat):
    """funcao recebe matriz e faz uma busca por setor,
       dado o nome de um setor da empresa,função retorna os dados 
       de todos os func.do setor
       
    """
    lista=[]
    
    for i in mat:
        if i[2]==setor:
            i.remove(setor)
            lista.append(i)
    return lista