import math
def total (lista,produtos):
     soma = 0
     prod = list(produtos.items())
     for prod in lista:
        soma = soma + produtos[prod]
     #soma = int(math.floor(soma))
     format(soma,".4f")
     return soma
# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis