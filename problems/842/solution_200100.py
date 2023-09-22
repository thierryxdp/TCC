"""
Nesta questão, o principal princípio utilizado foi acessar listas dentro de listas
possibilitando que comparássemos os números de gols e chegarmos no resultado 
desejado. Assim foram criados parâmetros que ao serem confirmados, geram a nossa
resposta.
list -> dict
"""
def pontos_por_time(pontos):
    vit1A = pontos[0][2][0] > pontos[0][2][1]
    vit1B = pontos[0][2][1] > pontos[0][2][0]
    emp1 = pontos[0][2][0] == pontos[0][2][1]
    vit2A = pontos[1][2][1] > pontos[1][2][0]
    vit2B = pontos[1][2][0] > pontos[1][2][1]
    emp2 =  pontos[1][2][0] == pontos[1][2][1]
    if vit1A and vit2A == True:
    	return {pontos[0][0]: 6, pontos[0][1]: 0}
    elif vit1B and vit2B == True:
        return {pontos[0][0]: 0, pontos[0][1]: 6}
    elif vit1A and emp2 == True:
        return {pontos[0][0]: 4, pontos[0][1]: 1}
    elif vit2A and emp1 == True:
        return {pontos[0][0]: 4, pontos[0][1]: 1}
    elif vit1B and emp2 == True:
        return {pontos[0][0]: 1, pontos[0][1]: 4}
    elif vit2B and emp1 == True:
        return {pontos[0][0]: 1, pontos[0][1]: 4}
    elif emp1 and emp2 == True:
        return {pontos[0][0]: 2, pontos[0][1]: 2}
    elif vit1A and vit2B == True:
        return {pontos[0][0]: 3, pontos[0][1]: 3}
    elif vit1B and vit2A == True:
        return {pontos[0][0]: 3, pontos[0][1]: 3}
    else:
        return 'Reprovei na matéria'