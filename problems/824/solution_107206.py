def uppCons (frase):
    """Função que, dada uma frase, retorna a mesma frase com todas suas consoantes em maiúsculas
    entrada: str
    saída: str"""
    
    nova_frase = ''
    proximo = 0
    
    while proximo < len(frase):
        if frase[proximo] not in 'AEIOUaeiou':
            nova_frase = nova_frase + str.upper(frase[proximo])
        proximo = proximo + 1
            
        if frase[proximo] in 'AEIOUaeiou':
            nova_frase = nova_frase + frase[proximo]
        proximo = proximo + 1
            
    return nova_frase