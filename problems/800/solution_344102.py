# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def total(list=[],dict={}):
    '''funçao que recebe uma lista de compras e um dicionarios com
    o preço de cada produto disponivel na loja e retorna o valor total
    dos itens da lista que estejam disponiveis nessa lista;
    list,dict-> float'''
    valor_total=0
    for i in list:
        valor_total = valor_total + dict[i]
    return round(valor,2)