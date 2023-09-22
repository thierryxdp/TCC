def uppCons(frase):
    '''Retorna a frase de entrada com todas as suas consoantes em letra
       maiúscula, permanecendo os demais caracteres inalterados;
       str -> str'''
    count=0
    fraseRetorno=''
    while count < len(frase):
        if frase[count] not in 'AEIOUaeiou':
            fraseRetorno+=frase[count].upper()
        else:
            fraseRetorno+=frase[count]
        count+=1
    return fraseRetorno