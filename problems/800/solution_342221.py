# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def total(produto,preco):
    '''recebendo uma lista de compras e uma outra entrada de dicionário contendo
o preço dos produtos em determinada loja retorno o valor total dos itens
disponéveis na loja'''
    valor = 0
    for prod in produto:
        valor=valor + preco[prod]
    return roun(valor,2)