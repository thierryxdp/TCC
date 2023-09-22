# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def total(compras,valores):
    soma = 0
    for i in valores:
        if i in compras:
            soma = soma + valores[i]
    return soma