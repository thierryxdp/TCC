def uppCons (frase):
    '''Função retorna a frase com todas as consoantes em maísculo (preservando os demais caracteres).;
    str -> str.'''
    indice = 0
    nova_frase = ''
    
    while indice < len (frase):
        if frase[indice] not in 'aeiouAEIOUáàãâéèêíìôõúùû':
            nova_frase = nova_frase + str.upper (frase [indice])
        else:
            nova_frase = nova_frase + frase[indice]
        indice = indice +1
    return nova_frase