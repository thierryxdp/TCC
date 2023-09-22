def filtra_pares(numeros):
    '''função que retorna apenas os elementos pares da tupla original(a,b,c,d= elementos inteiros)
      int,int,int,int->bool'''
    a=int(numeros[0:3])
    b=int(numeros[3:6])
    c=int(numeros[6:9])
    d=int(numeros[9:])
  
    tupla=()
    if a%2==0:
        tupla=tupla + ("a",)
    if b%2==0:
        tupla=tupla + ("b",)
    if c%2==0:
        tupla=tupla + ("c",)
    if d%2==0:
        tupla=tupla + ("d",)
    return tupla