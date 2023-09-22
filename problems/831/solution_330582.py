def lingua_p(palavra):
    """
    Função que recebe uma palvra e retorna ela traduzida para a língua do p.
    str -> str
    """
    palavra1 = palavra.lower()
    vogais = 'aeiou'
    
    for letra in palavra1:
        if letra == vogais:
            palavra1 = letra + 'p'
       	else:
            palavra1 = letra
    return palavra1