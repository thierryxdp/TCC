def faltante(l):
    """Retorna o número que está faltando no intervalo;
list -> int"""
    proximo = 0
    list.reverse(l)
    n = l[0]
    soma = 0 
    list.sort(l)
    
    if 1 not in l:
        return 1
    
    while proximo <= len(l):
        soma = soma + proximo + 1
        proximo = proximo + 1
        
    falta = soma - sum(l)
    
    return falta