def quant_palavras(frase):
    temp = str.split(frase, " ")
    if temp[0] == "":
        del temp[0]

    if temp[len(temp)-1] == "":
        del temp[len(temp)-1]
    
    return len(temp)

ex1 = " chaves e valores é utilizando o método dict. items(). A saída equivale a uma lista com elementos organizados em tuplas, sendo: O primeiro elemento da tupla a chave do dicionário e. "
ex2 = "Alguns vão te odiar, fingem que te amam agora. Então, pelas costas, eles tentam te eliminar. Mas quem Jah abençoa, ninguém amaldiçoa."
ex3 = "Se Deus criou as pessoas para amar e as coisas para cuidar, por que amamos as coisas e usamos as pessoas?"

quant_palavras(ex1)
quant_palavras(ex2)
quant_palavras(ex3)