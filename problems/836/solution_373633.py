def busca(setor,matriz):
    """
    recebe uma string com o nome de um setor e uma matriz no formato
    apresentado e retorna uma busca de todos os funcionários que
    trabalham nesse setor.
    """
    resultado=[]
    
    for linha in matriz:
        if linha[2]==setor:
            func=linha
            del func[2]
            list.append(resultado,func)
    return resultado