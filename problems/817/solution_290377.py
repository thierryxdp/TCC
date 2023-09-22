def faltas(lista):
    """ Função que recebe uma lista no seguuinte formato: [['Brasil', 'Italia', [10, 9]], ['Brasil', 'Espanha',[5, 7]], ['Italia', 'Espanha', [7,8]]]
    	Esta lista indica o número de faltas que cada time fez em cada jogo
        Dada a lista a função retorna o número de faltas do campeonato
        list-> int
    """
    faltas = sum([ falta [2][i] for falta in lista[:] for i in (0,1)] )
    
    return faltas