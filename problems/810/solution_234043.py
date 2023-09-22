def inverte(x):
    "função que dado uma string, retorna outra string com as mesmas palavras na ordem, inversa, todas as letras minuscúlas e sem pontuação."
    x = str.replace(x,"-"," ")
    x = str.replace(x,","," ")
    x = str.replace(x,":"," ")
    x = str.replace(x,";"," ")
    x = str.replace(x,"."," ")
    x = str.replace(x,"!"," ")
    x = str.replace(x,"?"," ")
    x = str.split(x)[-1::-1]
    x = str.join(" ",x)
    return str.lower(x)