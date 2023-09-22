def uppCons(frase):
    """função que retorna uma frase com todas as consoantes maiúscula, através da frase d eentrada;
    Entrada: str
    Saída: str"""
    f = []
    i = 0
    
    while not i == len(frase):
        if frase[i] != 'AEIOUaeiou':
            str.upper(frase[i])
            list.append(f,frase[i])
        i = i + 1
    return f