# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def total (lista,produtos):
     soma = 0
     produto = list(produtos.items())
     for produto in lista:
        soma = soma + produtos[produto]
     k = round(soma, 2)
     return k