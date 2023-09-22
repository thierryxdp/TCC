def uppCons(frase):
    '''Função que retorna uma frase com todas as consoantes 
    maiúsculas; recebe uma frase como entrada; String-->
    String'''
    i=0
    frase_nova=''
    while i<len(frase):
		if not frase[i] in 'aeiouAEIOUÃãáéíóúÁÉÍÓÚ':
            frase_nova+=str.upper(frase[i])
        else:
            frase_nova+=frase[i]
        i=i+1
    return frase_nova