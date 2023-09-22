# Funcao que retorna o total dos itens da lista que estao na loja
# Escolha nomes elucidativos para suas variáveis
def total(lista,valores):
    conta = 0.0
    for elem in range(0,len(lista)):
        if lista[elem] in valores:
            conta = conta + valores[lista[elem]]
    return round(conta,2)