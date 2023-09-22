def lingua_p(palavra):
    nova_palavra:''
    for i in range(len(palavra)):
        if palavra[i] in 'aeiouAEIOU':
            nova_palavra = nova_palavra + palavra[i] + 'p'
        else:
            nova_palavra = nova_palavra + palavra[i]
    return nova_palavra