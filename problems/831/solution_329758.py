def lingua_p(palavra):
    '''Funcao que, dada uma palavra, retorna essa palavra na lingua do p, ou seja, apos cada vogal, e inserido o p e em seguida a propria vogal; str -> str'''
    str.lower(palavra)
    i=0
    nova_str=''
    while i<len(palavra):
        if 'a' in palavra:
            nova_str=str.replace(palavra,'a','apa')
        elif 'e' in palavra:
            nova_str=str.replace(palavra,'e','epe')
        elif 'i' in palavra:
            nova_str=str.replace(palavra,'i','ipi')
        elif 'o' in palavra:
            nova_str=str.replace(palavra,'o','opo')
        elif 'u' in palavra:
            nova_str=str.replace(palavra,'u','upu')
        i=i+1
    return nova_str