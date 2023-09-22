def filtra_pares(tupla):
    """Retorna os elementos pares com uma tupla"""
    #Entrada precisa ser em forma de tupla
    elemento1=(tupla[0],)
    elemento2=(tupla[1],)
    elemento3=(tupla[2],)
    elemento4=(tupla[3],)
    tuplaPar=()
    resto1=tupla[0]%2
    resto2=tupla[1]%2
    resto3=tupla[2]%2
    resto4=tupla[3]%2
    if resto1==0:
        tuplaPar+=()+elemento1
    if resto2==0:
         tuplaPar+=()+elemento2
    if resto3==0:
          tuplaPar+=()+elemento3
    if resto4==0:
           tuplaPar+=()+elemento4
    return tuplaPar