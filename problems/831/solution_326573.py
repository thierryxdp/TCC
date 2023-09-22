def lingua_p(palavra):
    """Dada uma palavra a retorna na língua do P."""

    palavra = str.lower(palavra)
    palavra_final = ''
    vogais = 'aeiouáéíóúàèìòùãõâêîôû'

    for i in palavra:
        palavra_final += i
        if i in vogais:
            palavra_final = palavra_final + 'p' + i
            
    return palavra_final