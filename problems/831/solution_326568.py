def lingua_p(palavra):
    '''Função que recebe como entrada uma palavra em português e retorna a
    tradução para a língua do P.'''
    palavra = str.lower(palavra)
    palavra_nova = ''
    vogais = 'aeiouáéíóúãõàèìòùâêîôû'
    for letra in palavra:
        palavra_nova += letra
        if letra in vogais:
            palavra_nova += 'p' + letra
    return palavra_nova