# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(l1, l2):
    """Função que intercala elementosd de duas listas
    ass: list,list --> list
    testes:
    intercala([2,8,6],[5,2,1])==[2,5,8,2,6,1])
    intercala([7,2,4],[1,1,1])==[7,1,2,1,4,1])"""
    ret=[]
    ret=l1[0],l2[0],l1[1],l2[1],l1[2],l2[2]
    return ret