# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Função que dado duas listas de tamanho 3 gera uma outra lista com os elementos das primeiras duas intercalados."""
    if len(lista1)==3 and len(lista2)==3:
        return [lista1[0],lista2[0],lista1[1],lista2[1],lista1[2],lista2[2]]
    else:
        return "as lista dadas como parâmetro devem ter 3 elementos!"