# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medida, H, L):
    """Essa função irá dizer o colchão passará ou não pela porta de acordo com as medidas
    informadas nas variáveos. 
    Entrada: Lista | Saída: Boleano
    """
    list.sort(medida,reverse = True)
    if ((medida[0] > H and medida[1]>L) and (medida[1]>H and medida[0]>L)):
        return False
    else:
        return True