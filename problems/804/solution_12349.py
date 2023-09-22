def pares (n):
    '''assume n um número inteiro e se a / der resto 0
    conclui que é um numero par
    int -> float'''
    return (n % 2) == 0

def filtra_pares(tupla):  #inserir a tupla
    '''assume que recebe uma tupla com 4 elementos e, a partir
 deles serão filtrados e retornados apenas os pares
 tupla -> tupla'''
    tupla_vazia = () #modelo a ser analisado
    t = (t[],)
    
    if pares(t[0]):
   	 tupla_vazia = tupla_vazia + (t[0],)
    
    if pares (t[1]):
     tupla_vazia = tupla_vazia + (t[1],)
    
    if pares (t[2]):
     tupla_vazia = tupla_vazia + (t[2],)
    
    if pares (t[3]):
     tupla_vazia = tupla_vazia + (t[3],)
    
    return tupla_vazia (tupla)