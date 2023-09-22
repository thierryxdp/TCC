def lingua_p(palavra):
    palavra = list(palavra.lower())
    k = 0
    for i in palavra:
        if i in 'aeiouáéíóãõâêô':
            palavra.insert(k+1, 'p{}'.format(i))
        k += 1
    palavra_p = ''.join(palavra)
    return palavra_p