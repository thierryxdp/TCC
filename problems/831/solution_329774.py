def lingua_p(palavra):
    '''Funcao que, dada uma palavra, retorna essa palavra na lingua do p, ou seja, apos cada vogal, e inserido o p e em seguida a propria vogal; str -> str'''
    str.lower(palavra)
    nova_str=''
    for letra in palavra:
        if letra in 'aeiou':
            nova_str=str.replace(palavra,'a','apa')
            nova_str=str.replace(palavra,'e','epe')
            nova_str=str.replace(palavra,'i','ipi')
            nova_str=str.replace(palavra,'o','opo')
            nova_str=str.replace(palavra,'u','upu')
        return nova_str