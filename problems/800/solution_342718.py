# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def total(lista,dicionario):
    '''calcula o valor da compra de todos os itens da lista.
    lista,dicionario->float'''
    a=0
    for i in range(len(lista)):
        if lista[i] in dicionario:
            a+=dicionario[lista[i]]
    return round(a,2)