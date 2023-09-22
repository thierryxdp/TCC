# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def total(lista,dicio):
    soma=0
    for i in lista:
        if i in dicio:
            soma+=dicio.get(i)
    return round(soma,2)