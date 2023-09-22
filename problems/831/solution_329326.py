def lingua_p(frase):
    nova_frase:''
    for i in range(len(frase)):
        if frase[i] in 'aeiouAEIOU':
            nova_frase = nova_frase + frase[i] + 'p'
        else:
            nova_frase = nova_frase + frase[i]
    return nova_frase