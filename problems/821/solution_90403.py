def fatorial(numero):
    '''recebe um número e retorna o fatorial dele.'''
    i=numero-1
    #Verifica enquanto I for maior do que 0 
    while i>0:
        #decrementa o número e múltiplica
        numero*=i
        i-=1
    return numero