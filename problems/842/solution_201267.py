def competicao(nomepontuacao,competidor):
    """
        Função que dado um dicionário com o nome dos competidores,  pontuação
        e dado também o nome do competidor que esteja no dicionário
        retorna a classificação do mesmo.
        dict, str -> int
    Entrada:
             dicionário, string
    Saída:
            número inteiro - int
    """ 
    
    p = len(nomepontuacao)
    pontuacao = list(nomepontuacao.values())
    pontuacao.sort()
    pontuacao.reverse()
    i = pontuacao.index(nomepontuacao[competidor])
    r= i+1
    return r#Start your python function here