# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def total(Lcompras, D_preco_prod):
    '''
        Funcao recebe uma lista de compras e um dicionario
        contendo o preco de cada produto disponivel em uma loja
        e retorna o valor total dos itens da lista que estejam
        disponiveis na loja.
        list, dict -> float
        
    '''
    precos = 0
    
    for produto in Lcompras:
        precos = round((precos + dict.get(D_preco_prod,produto)),2)
    return precos