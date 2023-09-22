def uppCons (frase):
    """Função que, dada uma frase, retorna a frase com todas as suas consoantes em maiúsculas e os demais caracteres como estavam na frase original
    entrada: str
    saída: str"""
    
    proximo = 0
    
    while proximo < len ('frase'):
        if frase[proximo] not in 'AEIOUaeiou':
            proximo = proximo + 1
            frase[proximo] = str.upper(frase[proximo])
    
        return frase