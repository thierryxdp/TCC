def lingua_p(palavra):
    """
    Função que recebe uma palvra e retorna ela traduzida para a língua do p.
    str -> str
    """
    vogais = 'aeiou'
    letrap = ''
    
    for letra in palavra: 
        if letra in vogais:
            letrap = letrap + letra + 'p' + letra + palavra
        else:
            letrap = letrap + letra 
            
    return letrap