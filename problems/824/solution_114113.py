def uppCons(frase):
    """Função que recebe como entrada uma frase e retorna-a com as consoantes em caixa alta."""
    """string->string"""
    i=0
    consoante="aeiouáéíóúàèìòùâêîôû"
    while i<len(frase):
        if frase[i] not in consoante:
            frase = str.replace(frase,frase[i],str.upper(frase[i]))
        elif frase in consoante:
            frase = frase
        i=i+1
    return frase