def colchao(lista,H,L):

    '''Calcula e retorna se o cochao passa ou n pela porta, dado os dados de entrada(lista contendo as medidas do colchao comprimento,largura e altura,a largura e altura da porta""" '''

    ''' lista, int,int-bol''' 

    lista2=[H,L]

    h=lista[1:2]

    l=lista[-1:]

    H1=lista2[0:1]

    L2=lista2[-1:]

    if h<=H1 or l<=L2:

        return True

    else:

        if h>H1 and l>L2:

            return False