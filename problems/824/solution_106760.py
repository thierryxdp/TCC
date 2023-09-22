def uppCons(frase):
    '''Função que dada uma frase, retorna a mesma porém com todas as consoantes em maiúsculas
    str -> str'''
    vogais='aeiouAEIOUáéíóúÁÉÍÓÚâêîôûÂÊÎÔÛãÃ'
    i=0
    frase_nova=''
    while i<len(frase):
        if frase[i] not in vogais:
            frase_nova+=str.upper(frase[i])
        else:
            frase_nova+=frase[i] 
        i+=1
    return frase_nova