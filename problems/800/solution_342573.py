# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def total (lista,produtos):
     compras = 0
     preco = produtos.values()
     for produtos in lista:
          compras = sum(preco)
     return compras