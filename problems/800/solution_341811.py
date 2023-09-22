# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def total(lista_de_compras,precos):
    '''Função que retorna valor total dos itens da lista disponíveis na loja.
    list,dict->float'''
    soma = 0
    for item in lista_de_compras:
        soma=soma+dict.get(precos,item,0)
    return round(soma,2)