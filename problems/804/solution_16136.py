def paridade(n):
    """ Recebe um número 'n' e retorna True se ele for par. Caso contrá-
    rio, retornará False.
    Entrada: Float
    Saída: Bool
    """
    return n%2==0

def filtra_pares(tupla):
    """ Função que recebe uma tupla com quatro elementos inteiros como
    parâmetro e retorna uma nova tupla contendo apenas os elementos pares
    da tupla original, na mesmo ordem em que se encontravam.
    Entrada: tupla
    Saída: tupla
    """
    nova_tupla = ()
        
    if paridade(tupla[0]):
        nova_tupla = nova_tupla + (tupla[0],)
    if paridade(tupla[1]):
        nova_tupla = nova_tupla + (tupla[1],)
    if paridade(tupla[2]):
        nova_tupla = nova_tupla + (tupla[2],)
    if paridade(tupla[3]):
        nova_tupla = nova_tupla + (tupla[3],)
            
    return nova_tupla