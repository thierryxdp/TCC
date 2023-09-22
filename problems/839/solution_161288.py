def carros(Pessoas,Lugares):
    razao = Pessoas/Lugares
    if razao!=0:
        return (Pessoas//Lugares)+1
    else:
        return Pessoas//Lugares