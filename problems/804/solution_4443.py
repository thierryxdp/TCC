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
    elif p[0]%2==0 and p[1]%2==0:
        return p[0:2]
    elif p[0]%2==0 and p[1]%2==0 and p[2]%2==0:
        return p[0:3]
    elif p[0]%2==0 and p[1]%2==0 and p[2]%2==0 and p[3]%2==0:
        return tupla