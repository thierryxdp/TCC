def lingua_p(palavra):
    ''' Entrada: palavra -> dado do tipo string
    	
        Saída: a palavra de entrada taduzida pa a língua do P, 
        	  ou seja, após cada vogal palavra original, será 
              inserida a sequência de letras 'p' mais a vogal original
        
        Obs: a resposta ignora a diferença entre maiúsculas e 
        minúsculas e retorna traduzida toda em minusculas
        
        str -> str'''
    texto = list(texto_minusculo)
    frase_linguaP = []
    for letra in texto:
        if letra in 'aeiouàáéíóú':
            frase_linguaP = frase_linguaP + list(letra) + list('p') + list(letra)
        else:
            frase_linguaP = frase_linguaP + list(letra)
        frase_linguaP = (''.join(frase_linguaP))
        return frase_linguaP
    else: 
        return texto_minusculo