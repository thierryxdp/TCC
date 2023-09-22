# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis

def total(lista, dicionario):
    valor=0
    for key in dicionario:
        if key in lista:
            valor+=dicionario[key]
    return valor