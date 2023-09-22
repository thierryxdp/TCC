# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(list1, list2):
    ''' Função que dada duas listas de tamanho 3, gere uma terceira lista intercalando seus elementos
    os tipos de entradas list-list-> list'''
    list3= list1[0:1]+list2[0:1]+list1[1:2]+list2[1:2]+list1[2:]+list2[2:]
    return list3