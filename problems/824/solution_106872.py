def uppCons (frase):
    """Função que, dada uma frase como entrada, retorna a mesma frase, mas com todas as 
    consoantes em letra maiúscula.
    Entrada: string.
    Saída: string."""
    
    i = 0
    consoante = ''
    
    while i < len(frase):
        if frase[i] in "AEIOUaeiou":
        	consoante = consoante + frase[i]
        else:
            consoante = consoante + str.upper(frase[i])
        i = i+1
    return consoante