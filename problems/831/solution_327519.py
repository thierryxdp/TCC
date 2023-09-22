def lingua_p(palavra):
    '''Esta função, dada uma palavra em português, retorna
    esta na língua do P (após cada vogal da palavra original
    será inserida a letra p).
    str -> str'''
    
    nova_palavra=''
    palavra=str.lower(palavra)    
    
    for letra in palavra:
        if letra in 'aeiou':
            nova_palavra=nova_palavra+letra+str(p)
        else:
            nova_palavra=nova_palavra+letra
            
    return nova_palavra