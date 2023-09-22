def uppCons(frase):
    "Função que dada uma frase de entrada retorna a mesma frasa com as cosoantes em maiúsculo. str --> str"
    nova_frase=''
    i=0
    while i<len(frase):
        if frase[i] not in 'AÃÂÁÀEÉÈÊIÍÌÎOÓÒÕÔUÚÙÛaãâáàeêéèiîíìoõôóòuûúù':
            nova_frase=nova_frase+str.upper(frase[i])
        else:
            nova_frase=nova_frase+frase[i]
        i=i+1
    return nova_frase