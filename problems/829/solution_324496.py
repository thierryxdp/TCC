#Função que calcula e retorna o valor H com N termos onde N é inteiro com o resultado somente com 2 casas decimais
def soma_h(n):
    contador = 1
    lista = 0
    tamanho = range(n+1)
    if n == 1:
        return 1
    while contador < n+1:
          lista = lista + 1/tamanho[contador]
          contador = contador + 1

    return round(lista,2)