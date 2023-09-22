def primo(numero):
    primo=0
    resultado=''
    
    for valor in list(range(1,numero+1)):
        x=numero/valor
        primo=int((x/x)+primo)
        if primo==2:
            resultado=True
        if primo!=2:
            resultado=False
    return resultado