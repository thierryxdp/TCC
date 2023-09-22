# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    '''
        Cria uma terciera lista (L3) concatenando duas listas recebidas (L1 e L2)
        list -> list
        lista1 e lista2: listas de numeros.
        L3: Lista derivada da concatenação das duas primeiras.
        
    '''
    L3=[str(lista1[0])+', '+str(lista2[0])+', '+str(lista1[1])+', '+str(lista2[1])+', '+str(lista1[2])+', '+str(lista2[2])]
    return L3