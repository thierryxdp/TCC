def uppCons(frase):
    """função que recebe uma frase e retorna a mesma com todas as suas consoantes maiúsculas;
    Entrada: str
    Saída: str"""
    i = 0
    
    while not i == len(a):
        if (frase[i]) != 'aeiouAEIOU':
            str.replace(frase, frase[i],str.upper(frase[i])) 
        i = i + 1
    return frase