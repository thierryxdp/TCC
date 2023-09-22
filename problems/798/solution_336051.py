def freq_palavras(frase):
    """Recebe uma string e retorna um dicionário, onde cada palavra da string
é uma chave que tem como valor o número de vezes que a palavra aparece;
str -> dic"""
    palavras = str.split(frase)
    dici_frequencia = {}
   
    for elemento in palavras:
        frequencia = list.count(palavras, elemento)
        dici_frequencia[elemento] = frequencia
        
    return dici_frequencia