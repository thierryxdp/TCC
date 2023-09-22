# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def total (lista_compras,produtos):
    ''' '''
    i=0
    w=0
    soma=0
    for i in range(0, len(lista_compras)):
          for w in range(0, len(produtos)):
            if (lista_compras[i]) == (list(produtos)[w]):
                  soma = soma + produtos[lista_compras[i]]
                	w=w+1
             i=i+1
    soma = round(soma,2)
    return soma