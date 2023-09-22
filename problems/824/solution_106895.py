def uppCons (frase):
    """Função que, dada uma frase, retorna a frase com todas as suas consoantes em maiúsculas e os demais caracteres como estavam na frase original
    entrada: str
    saída: str"""
    
    nova_frase = ''
    proximo = 0
    
    while proximo < len ('frase'):
        if frase[proximo] not in 'AEIOUaeiou':
            nova_frase[proximo] == str.upper(frase[proximo])
            proximo = proximo + 1
          
        if frase[proximo] in 'AEIOUaeiou':
            nova_frase[proximo] = frase[proximo]
            proximo = proximo + 1
            
    return nova_frase