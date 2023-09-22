def lingua_p(word):
    '''Função que retorna essa palavra na lingua do p.'''
    '''str->str'''
    nova_palavra = ""
    for elemento in word:
        if elemento in "aeiouAEIOUáéíóú":
            nova_palavra = nova_palavra + elemento + "p" + elemento
        else:
            nova_palavra = nova_palavra + elemento
           return nova_palavra