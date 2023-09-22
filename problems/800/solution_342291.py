# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def total(lista_de_compras,produtos):
    i=0
    for lista_de_compras[i] in produtos:
        T=sum(produtos[lista_de_compras[i]])
    i+=1
    return T