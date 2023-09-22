def pontos_por_time(lista):
    """função que recebe uma lista completa de informações do número de gols em dois jogos de futebol entre dois times e retorna o total de pontos dos times"""
    primeirotime=lista[0][0]
    segundotime= lista[0][1]
    golsdoprimeirotime=lista[0][2][0]
    golsdoprimeirotimefinal=lista[1][2][1]
    golsdosegundotime=lista[0][2][1]
    golsdosegundotimefinal=lista[1][2][0]
    pontosprimeirotime=0
    pontosegundotime=0
    vitoria=3
    empate=1
    if golsdoprimeirotime > golsdosegundotime:
        pontosprimeirotime+=vitoria
    if golsdoprimeirotimefinal> golsdosegundotimefinal:
        pontosprimeirotime+=vitoria
    if golsdosegundotime>golsdoprimeirotime:
        pontosegundotime+=vitoria
    if golsdosegundotimefinal>golsdoprimeirotimefinal:
        pontosegundotime+=vitoria
    if golsdoprimeirotime==golsdosegundotime:
        pontosprimeirotime+=empate
        pontosegundotime+=empate
    if golsdosegundotimefinal==golsdoprimeirotimefinal:
        pontosprimeirotime+=empate
        pontosegundotime+=empate

    return {primeirotime:pontosprimeirotime, segundotime:pontosegundotime}