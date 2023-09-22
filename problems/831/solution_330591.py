def lingua_p(palavra):
    """
    Função que recebe uma palvra e retorna ela traduzida para a língua do p.
    str -> str
    """
    vogais = 'aeiou'
    
    for letra in palavra: 
        if letra in vogais:
            palavra = letra + 'p' + palavra
    return palavra