def carros(p,c=5):
    """Calculoa o número de carros necessários para uma viagem de amigos"""
    if(p%c!=0):
        return int(p/c)+1
    else: 
        return p/c