def busca(setor, matriz):
    """Calcula e retorna os dados dos funcionarios de uma empresa representados
  	na matriz a partir da busca por setor; str,list"""
    filtragem=[]
    for i in matriz:
		if setor in i:
            filtragem=list.append(filtragem, i)
    return filtragem