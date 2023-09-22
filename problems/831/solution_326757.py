def lingua_p(palavra):
    "Traduz uma palavra para a lingua do p."""
    vogal = ['aeiou']
    for vogal in palavra:
        palavra.replace(vogal,'p'+vogal)
    return palavra