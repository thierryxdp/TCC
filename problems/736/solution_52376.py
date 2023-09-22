# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str, str -> str
def concatenacao(a, b):
    """Recebe duas datas e calcula a diferença em dias
    str, str-> int"""
    dia1 = int(data1[0:2])
    mes1 = int(data1[3:5])
    ano1 = int(data1[6:])
    dia2 = int(data2[0:2])
    mes2 = int(data2[3:5])
    ano2 = int(data2[6:])
    TotalDias = 0
    if (dia1==dia2) and (mes1 == mes2) and (ano1 == ano2):
        return TotalDias
    elif(ano1>ano2) or (ano1==ano2 and mes1>mes2) or (ano1==ano2 and mes1==mes2 and dia1>dia2):
        return TotalDias
    else:
        TotalDias = TotalDias + (dia2-dia1)
        TotalDias = TotalDias + (mes2-mes1)*30
        TotalDias = TotalDias + (ano2-ano1)*365
    return TotalDias