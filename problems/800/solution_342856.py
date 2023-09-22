# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def total(lista_de_compras, produtos):
    resultado=0
    for produto in lista_de_compras:
        resultado += produtos[produto]

        if resultado > 10:
            resultado = False
            return resultado
        else:
            resultado = True

    return resultado