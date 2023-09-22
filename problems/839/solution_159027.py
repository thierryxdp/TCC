def carros(numP, capacidadeV=5):
   	Ncarros = numP//capacidadeV
    if numP%capacidadeV > 0:
        return Ncarros + 1
    return Ncarros