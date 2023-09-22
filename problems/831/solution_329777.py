while i<len(palavra):
        if 'aeiou' in palavra:
            nova_str=str.replace(palavra,'a','apa')
            nova_str=str.replace(palavra,'e','epe')
            nova_str=str.replace(palavra,'i','ipi')
            nova_str=str.replace(palavra,'o','opo')
            nova_str=str.replace(palavra,'u','upu')
        i=i+1
    return nova_str