# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Função que dadas duas listas de tamanho 3, gera uma terceira lista que é formada intercalando os elementos das outras duas listas.  ent-> lista   saida -> lista"""
    
    intercalada = []
    for a,b in zip(lista1, lista2):
        intercalada.append(a)
        intercalada.append(b)
    return intercalada