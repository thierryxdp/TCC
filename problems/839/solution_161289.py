def carros(Pessoas,Lugares=5):
    razao = Pessoas/Lugares
    if razao!=0:
        return (Pessoas//Lugares)+1
    else:
        return Pessoas//Lugares