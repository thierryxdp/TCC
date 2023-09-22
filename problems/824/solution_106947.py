def uppCons(frase):
    '''função que recebe uma frase e retorna a mesma frase, mas com todas
    as consoantes em maiúsculas; str -> str'''
    frase = f
    i = 0
    while i < len(f):
        if f[i] not in 'AEIOUaeiouÁÀÂÃÉÊÍÓÔÕÚáàâãéêíóôõú':
            f = str.replace(f,f[i],str.upper(f[i]))
        i = i + 1
    return f