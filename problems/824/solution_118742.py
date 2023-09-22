def uppCons(frase):
    '''
    Funcao que recebe uma frase com entrada, e retorna outra frase com todas suas consonantes en maiusculas
    (e os demais caracteres exatamente com estavam na frase original)
    str -> str
    '''
    con = 0
    uppCons = ''
    while (con<len(frase)):
        caractere = frase[con]
        if caractere not in 'AEIOUaãáeéiíoóõuú':
            novo_car = caractere.upper()
        else:
            novo_car = caractere
        uppCons = uppCons + novo_car  
        con = con + 1
    return uppCons