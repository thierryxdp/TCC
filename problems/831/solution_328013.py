def lingua_p(palavra):
    """função que recebe uma palavra e retorna essa mesma
    palavra traduzida para a língua do P, onde após cada
    vogal da palavra original, é insedira a letra 'p' mais 
    a vogal original.
    str -> str"""

    nova_palavra = ''

    for letra in palavra:
        if letra not in 'aeiouAEIOUáéíóúãõâêîôû':
            nova_palavra += letra
        else:
            nova_palavra += letra + 'p' + letra
            
    return nova_palavra.lower()