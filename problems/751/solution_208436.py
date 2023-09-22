# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Função que dadas duas listas de tamanho 3 é formada
    uma nova lista intercalando os elementos das duas
    lista-> lista"""
    lista = [] 
    lista.append ( lista1 [ 0 ] ) 
    lista.append ( lista2 [ 0 ] )
    lista.append ( lista1 [ 1 ] )
    lista.append ( lista2 [ 1 ] )
    lista.append ( lista1 [ 2 ] )
    lista.append ( lista2 [ 2 ] )
    return lista