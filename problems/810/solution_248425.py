def altera_frase(frase, palavra, posicao):
     """Função que receba uma frase, uma palavra e uma posição 
     e retorne uma frase; string,int,string => string"""
        
    frase = frase.split(' ')
    if(palavra in frase):
        indice = frase.index(palavra)
        frase[indice] = palavra.upper()
    else:
        frase.insert(posicao, palavra)

    frase = ' '.join(frase).lstrip()
    return frase