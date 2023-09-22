def uppCons(frase):
    frasenova=''
    i=0
    while i<len(frase):
        if frase[i] in 'qwrtyipsdfghjklçzxcvbnm':
            frasenova= frasenova + frase[i]
        i=i+1
    return frasenova