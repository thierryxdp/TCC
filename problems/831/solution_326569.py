def lingua_p(palavra):
    '''
    '''
    palavra = palavra.lower() #Para facilitar, vou transformar as letras maiúsculas em minúsculas.
    palavra_na_lingua_p = ''
    vogais = 'aeiouáéíóúàèìòùâêîôûãõ' 
    for letra in palavra:
        palavra_na_lingua_p += letra 
        if letra in vogais:
            palavra_na_lingua_p = palavra_na_lingua_p + 'p' + letra
    return palavra_na_lingua_p