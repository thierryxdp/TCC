def busca(setor, matriz):
    """Calcula e retorna os dados dos funcionarios de uma empresa representados
  	na matriz a partir da busca por setor; str,list"""
    filtragem=[]
    for i in matriz:
        for setor in i:
           	filtragem=filtragem + list.del([i],setor,2)
    return filtragem