#
#
#
#
def uppCons(frase):
    i=0
    nova_frase=''
    while i < len(frase):
        if not frase[i] in 'AEIOUaeiou':
            str.upper(frase[i])
            nova_frase=nova_frase+frase[i]
        i=i+1
    return frase