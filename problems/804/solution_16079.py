def paridade(n):
    """ Recebe um número 'n' e retorna True se ele for par. Caso contrá-
    rio, retornará False.
    Entrada: Float
    Saída: Bool
    """
    return n%2==0

def filtra_pares(t):
    """ Função que recebe uma tupla com quatro elementos inteiros como
    parâmetro e retorna uma nova tupla contendo apenas os elementos pares
    da tupla original, na mesmo ordem em que se encontravam.
    Entrada: tupla
    Saída: tupla
    """
    
    nova_tupla:()
        
    if paridade(t[0]):
        nova_tupla = ()+t[0]
    if paridade(t[1]):
        nova_tupla = ()+t[1]
    if paridade(t[2]):
        nova_tupla = ()+t[2]
    if paridade(t[3]):
        nova_tupla = ()+t[3]
            
    return nova_tupla