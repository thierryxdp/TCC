def inverte(x):
    x = str.replace(x, "-"," ")
    x = str.replace(x, ","," ")
    x = str.replace(x, ":"," ")
    x = str.replace(x, ";"," ")
    x = str.replace(x, "."," ")
    x = str.replace(x, "?"," ")
    x = str.replace(x, "!"," ")
    x = str.replace(x, "..."," ")
    x = str.lower(x)

    lista = str.split(x)
  
    return str.join(" ",lista[::-1])