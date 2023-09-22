import round
def total (lista,produtos):
     soma = 0
     prod = list(produtos.items())
     for prod in lista:
        soma = soma + produtos[prod]
     round(soma, 2)
     return soma
# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis