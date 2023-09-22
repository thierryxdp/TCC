def lingua_p(palavra):
    "Traduz uma palavra para a lingua do p."""
    vogal = 'aeiouáéíóú'
    for indice in vogal:
        palavra = palavra.replace(indice,indice +'p'+ indice)
    return palavra