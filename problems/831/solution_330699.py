def lingua_p(palavra):
    '''Função que recebe uma palavra e retorna ela traduzida na língua do p.'''
    '''str->str'''
    nova = ""
    i = 0
    while i< len(palavra):
        list(palavra)
        if palavra[i] in "AEIOUaeiou":
            nova = nova + palavra[i] + "p" + palavra[i]
        i = i + 1
    return str.lower(nova)