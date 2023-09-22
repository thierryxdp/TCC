# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def total(lista,dicionario):
    a=list(dict.keys(dicionario))
    soma=0
    for i in lista:
        soma=soma+dicionario[i]
    return soma