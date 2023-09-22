# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Coloque um comentário dizendo o que a função faz e quais são os parâmetros de entrada e saída"""
    def intercala(l1,l2):
    "dadas duas listas L1 e L2 de tamanho 3, gera uma lista L3 que é formada intercalando os elementos de L1 e L2  (list[str,str,str],list[str,str,str] --> list[str,str,str,str,str,str])"""
    return [l1[0],l2[0],l1[1],l2[1],l1[2],l2[2]]