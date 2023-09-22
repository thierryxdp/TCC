def busca(matriz, setor):
    "Função que recebe uma amtriz com dados de funcinários e um setor da empresa, e retona todos os funcionários deste setor."
    "list, str -> list"
    s = []
    for funcionario in matriz:
        copia = funcionario.copy()
        for inf in funcionario:
            if inf == setor:
                copia.remove(inf)
    	 		s += copia
    return s