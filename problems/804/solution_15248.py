def filtra_pares(s):
    """função que retorna somente os números 
    pares da tupla original
    tuple=>tuple"""
    #as 4 primeiras posições da tupla repassadas 
    #para as ultimas letras do alfabeto(w,x,y,z)
    w = s[0] 
    x = s[1] 
    y = s[2]
    z = s[3]
    tupla_final = ()
    if w%2==0:
        tupla_final=tupla_final + (w,)
    if x%2 == 0:
		tupla_final= tupla_final + (x,)
    if y % 2 == 0:
        tupla_final= tupla_final + (y,)
    if z % 2 ==0:
        tupla_final= tupla_final + (z,)
    
    return tupla_final