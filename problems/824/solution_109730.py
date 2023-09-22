def uppCons(frase):
    """"Função que recebe uma frasse (string) e transforma as consoantes em maiúsculas na saída
    sendo o dado de saída também uma string"""
    maiusculas=''
    vogais ='aeiouáéíóúâêîôûãõ'
    for letra in frase:
        if letra.lower() not in vogais:
            maiusculas+=letra.upper()
        else:
            maiusculas+=letra
    return maiusculas