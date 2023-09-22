# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Recebe duas listas de 3 itens cada e cria outra com os valores intercalados de cada uma.
    list,list->list"""
    l3=['','','','','','']
    l3[0]=lista1[0]
    l3[1]=lista2[0]
    l3[2]=lista1[1]
    l3[3]=lista2[1]
    l3[4]=lista1[2]
    l3[5]=lista2[2]
    return l3