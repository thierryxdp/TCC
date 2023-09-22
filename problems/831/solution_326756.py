def lingua_p(palavra):
    "Traduz uma palavra para a lingua do p."""
    for vogal in palavra:
        palavra.replace(vogal,'p')
    return palavra