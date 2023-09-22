#
#
#
#
def uppCons(frase):
    i=0
    nova_frase=''
    while i < len(frase):
        if not frase[i] in 'AEIOUaeiou':
            u=str.upper(frase[i])
            nova_frase=nova_frase+u
        i=i+1
    return nova_frase