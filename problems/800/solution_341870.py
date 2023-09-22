# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def total(lista,dicio):
    """
    list, dict -> float
    """
    soma = 0
    for produto in dicio:
        if produto in lista:
        	soma = soma + dicio[produto]
    return round(soma,2)