# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def passarColchao(dimensaoColchao,H,L):
    """Funcao que determina se um colchao de medidas a x b x c descritas na lista
    "dimensaoColchao" passa nas portas de dimensoes altuxa x largura em centimetros."""
    portaMaior = max(H,L)
    portaMenor = min(H,L)
    passa = True

    if (portaMaior < dimensaoColchao[1] or portaMenor < dimensaoColchao[0]):
        passa = False
        
    return passa