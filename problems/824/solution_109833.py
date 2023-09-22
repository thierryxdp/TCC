def uppCons (frase):
    """Função que recebe uma frase como entrada e retorna a frase com todas as suas consoates
    maiúsculas e os demais caracteres como estavam na frase original.
    str -> str"""
    i = 0
    while i < len(frase):
        if frase[i] not in 'AEIOUaeiouãÃÍíéÉÕõóÓúÚ':
            frase = str.replace(frase,frase[i],str.upper(frase[i]))
        i = i + 1
    return frase