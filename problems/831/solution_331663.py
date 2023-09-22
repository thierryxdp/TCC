def lingua_p(palavra):
    'descrição'
    palavra = palavra.lower()
    nova_palavra = ''
    for i in range(palavra):
        if 'aeiou' in palavra:
            nova_palavra = 'p' + palavra
        return nova_palavra