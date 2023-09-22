def uppCons(frase):
    """função que recebe uma frase e retorna a mesma com todas as suas consoantes maiúsculas;
    Entrada: str
    Saída: str"""
    i = 0
    
    while not i == len(frase):
        if not (frase[i]) in ' aeiouAEIOU':
            frase = str.replace(frase, frase[i],str.upper(frase[i]))
            i = i + i
    return frase