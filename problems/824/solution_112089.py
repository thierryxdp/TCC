def uppCons(frase):
    ''' Função que dada uma frase qualquer, retorna todas as
    consoantes em forma maiúscula. Os demais não são alterados.
    Entrada: str
    Retorno: str '''
    
    nova_frase = ''
    indice = 0
    while indice < len(frase):
        if frase[indice] in "AEIOUaeiou":
            nova_frase += frase[indice]
        if frase[indice] not in "AEIOUaeiou":
            nova_frase += str.upper(frase[indice])
        
        indice += 1
        
    return nova_frase