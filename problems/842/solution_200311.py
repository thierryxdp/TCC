#Stardef classificacao(cv, ce, cs, fv, fe, fs):
    """função que retorna qual dos dois times,Cormengo e Flaminthians,qual dos dois times está melhor classificado,dados os numeros de vitorias e empates e os saldos dos dois times"""
    if (3*(cv) + (ce))>(3*(fv) + (fe)):
        return "Cormengo"
    if (3*(cv) + (ce))<(3*(fv) + (fe)):
        return "Flaminthians"
    if (3*(cv) + (ce))==(3*(fv) + (fe))and((cs)>(fs)):
        return "Cormengo"
    if (3*(cv) + (ce))==(3*(fv) + (fe))and((cs)<(fs)):
        return "Flaminthians"
    if (3*(cv) + (ce))==(3*(fv) + (fe))and((cs)==(fs)):
        return "Empate"t your python function here