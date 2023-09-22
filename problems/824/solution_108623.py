def uppCons(frase):
    '''Escreva uma frase entre ''. A funcao retorna as consoantes
    dessa frase em maiusculas.
    str -> str'''
    i=0
    nova_frase=''
    while i<len(frase):
		if frase[i] in 'wrtypsdfghjklzxcvbnmWRTYPSDFGHQqJKLZXCVBNMçÇ':
    		nova_frase=nova_frase+str.upper(frase[i])
        else:
            nova_frase=nova_frase+frase[i]
        i=i+1
    return nova_frase