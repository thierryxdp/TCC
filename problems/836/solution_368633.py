def busca(setor,matriz):
    """Realiza uma busca por setor, sendo assim retorna os dados de todos
       os funcionários do setor escolhido
       string, list --> list"""
    lista_setor = []
    
    for i in matriz:
        if i[2] == setor:
            i.pop(2)
            lista_setor.append(i)
    return lista_setor