# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(a,b,c,d,e,f):
    '''Função que forma e intercala uma lista l3,apartir de outras duas listas l1 e l2.
    exemplo:entra l1[2,4,7] e l2[3,5,6]; saída l3[2,3,4,5,6,7]. lis,lis->list'''
    lista1=[a,b,c]
    lista2=[d,e,f]
    lista3=lista1+lista2
    return sorted(lista3)