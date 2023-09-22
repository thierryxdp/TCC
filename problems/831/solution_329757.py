def lingua_p(palavra):
    '''Funcao que, dada uma palavra, retorna essa palavra na lingua do p, ou seja, apos cada vogal, e inserido o p e em seguida a propria vogal; str -> str'''
    str.lower(palavra)
    i=0
    nova_str=''
    while i<len(palavra):
        if palavra(i) =='a':
            nova_str=str.replace(palavra,'a','apa')
        elif palavra(i) =='e':
            nova_str=str.replace(palavra,'e','epe')
        elif palavra(i) =='i':
            nova_str=str.replace(palavra,'i','ipi')
        elif palavra(i) =='o':
            nova_str=str.replace(palavra,'o','opo')
        elif palavra(i) =='u':
            nova_str=str.replace(palavra,'u','upu')
        i=i+1
    return nova_str