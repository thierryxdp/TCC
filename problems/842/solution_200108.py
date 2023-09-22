def classificacao(cv, ce, cs, fv, fe, fs):
    """ Função que calcula e retorna a classificação de 2
    times de futebol de acordo com os pontos arrecadados em
    vitórias (3 pontos) e em empates (1 ponto) e em caso de
    empate final, pelo critério de saldo de gols."""
    if ((cv*3) + (ce*1)) > ((fv*3) + (fe*1)):
        return 'Cormengo'
    elif ((cv*3) + (ce*1)) < ((fv*3) + (fe*1)):
        return 'Flaminthians'
    elif cs > fs:
        return 'Cormengo'
    elif cs < fs:
        return 'Flaminthians'
    else:
        return 'Empate'