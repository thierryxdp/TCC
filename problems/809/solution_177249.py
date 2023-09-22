# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(listaA, listaB):
    """Coloque um comentário dizendo o que a função faz e quais são os parâmetros de entrada e saída"""
        '''listaA,listaB->listaC'''
    listaC = []
    for i in range (0,len (listaA)):
        listaC.append (listaA[i])
        listaC.append (listaB[i])
    return listaC