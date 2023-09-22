def uppCons (frase):
    """Função que, dada uma frase, retorna suas consoantes em maiúsculas
    entrada: str
    saída: str"""
    
    proximo = 0
    nova_frase = ''
    
    while proximo < len(frase):
        if frase[proximo] in 'AEIOUaeiouáàéíóòúãõ':
            nova_frase = nova_frase + frase[proximo]
            proximo = proximo + 1
            
        if frase[proximo] not in 'AEIOUaeiouáàéíóòúãõ':
            nova_frase = nova_frase + str.upper(frase[proximo])
            proximo = proximo + 1
        
    return nova_frase