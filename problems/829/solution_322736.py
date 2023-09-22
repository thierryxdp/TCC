def soma_h (lista,produtos):
     soma = 0
     preco = produtos.values()
     for produtos in lista:
        soma = sum(preco)
        round(soma,2)
     return soma