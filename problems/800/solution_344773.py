# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def total(lista,preco):
    '''função que recebe uma lista e um dicionario com os preços e retorna o valor
    total da lista 
    list,dic->int'''
    precos=[]
    for i in lista:
        if i in dict.keys(preco):
            precos.append(preco[i])
    return round(sum(precos),2)