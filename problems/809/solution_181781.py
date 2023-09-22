# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Função que intercala os elementos da lista1 e lista2; list,list -> list"""
    if len(lista1)>3 or len(lista2)>3:
        return "Esta função trabalha somente com duas listas com apenas 3 elementos."
    intercarlada=[lista1[0]]+[lista2[0]]+[lista1[1]]+[lista2[1]]+[lista1[2]]+[lista2[2]]
    return intercarlada