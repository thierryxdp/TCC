def posLetra(x,y,z):
    """funcao que dada uma palavra(x), uma letra(y) e um numero que indica a ocorrencia 
    desejada(z), retorna a posição da letra na palavra. str, str, str->int"""
    achar=x.find(y)
    while achar>=0 and z>1:
        achar=x.find(y, achar+1)
        z=-1
        return achar