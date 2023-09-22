def lingua_p(palavra):
    nova_lingua = ''
    for i in palavra:
        if i in 'aeiouáéíóúAEIOU':
            nova_lingua = nova_lingua + i + 'p' + i
        else: 
            nova_lingua = nova_lingua + i
        return nova_lingua