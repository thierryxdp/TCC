def carros(numP, capacidadeV=5):
   	Ncarros = numP//capacidadeV
    if Ncarros%capacidadeV > 0:
        Ncarros = Ncarros + 1
    return Ncarros