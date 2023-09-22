def inverte (x):
    """ funcao ira receber uma frase e inverter
    entrada: string
    saida: string"""
    x = str.replace (x, "-"," ")
    x = str.replace (x, ","," ")
    x = str.replace (x, ":"," ")
    x = str.replace (x, ";"," ")
    x = str.replace (x, "."," ")
    x = str.replace (x, "!"," ")
    x = str.replace (x, "?"," ")
    x = str.split (x) [-1::-1]
    x= str.join (" ",x)
    return (str.lower (x))