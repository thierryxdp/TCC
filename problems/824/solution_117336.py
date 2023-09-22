def uppCons(frase):
    '''função que retorna a frase com as suas consoantes em letra maiúscula, dado a frase; str->str'''
    indice=0
    nova_frase=''
    while indice<len(frase):
        if frase[indice] not in 'AEIOUaeiou':
            nova_consoante=str.upper(frase[indice])
            nova_frase=nova_frase+nova_consoante
        if frase[indice] in 'AEIOUaeiou':
            nova_frase=nova_frase+frase[indice]
        indice=indice+1
    return nova_frase