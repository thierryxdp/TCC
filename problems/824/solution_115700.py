def uppCons(frase):
    '''Função que recebe como entrada uma frase e a retorna com todas
    as suas consoantes maiúsculas'''
    i=0
    while i<len(frase):
        if not frase[i] in 'aeiouAEIOUáéíóúÁÉÍOÚ':
            frase=str.replace(frase,frase[i],str.upper(frase[i]))
        i=i+1
    return frase