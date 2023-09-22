def retira_pontuacao(frase):
    temp = str.replace(frase, ".", " ")
    temp = str.replace(temp, ";", " ")
    temp = str.replace(temp, ",", " ")
    temp = str.replace(temp, "/", " ")
    temp = str.replace(temp, "-", " ")
    temp = str.replace(temp, "_", " ")
    temp = str.replace(temp, ":", " ")
    temp = str.replace(temp, "!", " ")
    temp = str.replace(temp, "?", " ")
    temp = str.replace(temp, "(", " ")
    temp = str.replace(temp, ")", " ")
    temp = str.replace(temp, "\"", " ")
    return temp

def inverte(frase):
    temp = retira_pontuacao(frase)
    temp_list = str.split(temp, " ")
    list.reverse(temp_list)
    nova_frase = str.join(" ", temp_list)

    return nova_frase

ex1 = "chaves e valores é utilizando o método dict. items(). A saída equivale a uma lista com elementos organizados em tuplas, sendo: O primeiro elemento da tupla a chave do dicionário e."
ex2 = "Alguns vão te odiar, fingem que te amam agora. Então, pelas costas, eles tentam te eliminar. Mas quem Jah abençoa, ninguém amaldiçoa."
ex3 = "Se Deus criou as pessoas para amar e as coisas para cuidar, por que amamos as coisas e usamos as pessoas?"

inverte(ex1)
inverte(ex2)
inverte(ex3)