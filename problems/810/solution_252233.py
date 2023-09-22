def inverte(f):
 "inverte frase retirando a pontuacao e substituindo letras maiusculas por minusculas str-->str"
    f2= f.split(",")
    f2= ''.join(f2)
    f2= f2.split(".")
    f2= ''.join(f2)
    f2= f2.split("!")
    f2= ''.join(f2)
    f2= f2.split("?")
    f2=''.join(f2)
    f2= f2.split("-")
    f2= ' '.join(f2) 
    f2= f2.lower()
    f3= f2.split()[::-1]
    return' '.join(f3)