def uppCons(frase):
    ''' funcao que apos receber uma frase ela ira retornar uma outra frase
    contendo todas as suas consoantes em letra maisculas e as sua vogal e 
    pontuacao exatamente do jeito que estava. str -> str
    nova_frase = '''
    i = 0 
    while i<len(frase):
        if frase[i] not in 'AEIOUÃÁÂÉÍÓÕÚaeiouãáâéíóõú':
            nova_frase = nova_frase + frase[i].upper()
        else:
            nova_frase = nova_frase + frase[i]
        i=i+1
    return nova_frase