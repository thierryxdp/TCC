def primo(numero):
    """Recebe um número e retorna True caso ele seja primo
    e False caso não seja.
    Assinatura: int -> booleano"""
    contador=0
    divisores=[]
    while contador<=numero:
        contador+=1
        if numero%contador == 0:
            divisores.append(contador)     
    if divisores == [1,numero]:
        return True
    elif divisores != [1,numero]:
        return False