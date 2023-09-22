# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    
    ''' Essa função deve verificar se o colchão comprado de medidas 
    (AxBxC) passa pela porta (HxL)
    lista, int, int, bool '''
    
    a,b,c = medidas
    
    if b<=H:
        return True
    elif b<=L:
        return True
    else:
        return False