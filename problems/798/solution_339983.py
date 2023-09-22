def freq_palavras(frase):
    dictionary = dict(frase.split("=") for frase in str.split(";")) 
print(dictionary)