#Start your python function here
def fitra_pares(p):
    """Função que recebe uma tupla com quatro elementos inteiros e retorna
     uma nova tupla contendo apenas os elementos pares da tupla original,
     na mesma ordem em que se encontravam.
     
     tuple -> tuple
     
     Parameters:
     p: Tupla com quatro elementos do tipo int
     """
    tupla = ()
    if p[0]%2==0:
        tupla=tupla+(p[0],)
    if p[1]%2==0:
        tupla=tupla+(p[1],)
    if p[2]%2==0:
        tupla=tupla+(p[2],)
    if p[3]%2==0:
        tupla=tupla=(p[3],)
    return tupla