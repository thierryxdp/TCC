def busca(setor, matriz):
    """ Retorna as informações de todos os funcionários do setor.
    	str, list -> list
        
        Parameters:
        setor: String com o nome do setor.
       	matriz: Matriz com as listas de info dos funcionários.
        
        Returns:
        Lista com as informações de todos os funcionários do setor.
    """
    ret = []
    for i in matriz:
        if setor == i[2]:
            del i[2]
            ret.append(i)
    return ret