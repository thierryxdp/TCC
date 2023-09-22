def lingua_p(palavra):
    "Traduz uma palavra para a lingua do p."""
    vogal = 'aeiou'
    for indice in vogal:
        nova = palavra.replace(vogal,'p'+ vogal)
    return nova