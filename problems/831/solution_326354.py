def lingua_p(frase):
    """
    Função que recebe uma string e retorna essa
    string traduzida para a linguagem p
    
    str -- > str
    """
    
    frase=frase.lower()
    
    trad=''
    
    for letra in frase:
        trad+=letra
        
        if letra in 'aeiou':
            trad+='p'+letra
    return trad