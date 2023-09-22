def uppCons (frase):
    """Função que, dada uma frase, retorna a frase com todas as suas consoantes em maiúsculas e os demais caracteres como estavam na frase original
    entrada: str
    saída: str"""
    
    proximo = 0
    
    while proximo < len ('frase'):
        if frase[proximo] not in 'AEIOUaeiou':
            str.upper(frase[proximo])
            proximo = proximo + 1
    
     return frase