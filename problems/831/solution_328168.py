def lingua_p(palavra):
    """essa funcao recebe como parametro uma palavra (em portugues) e retorna esta mesma palavra traduzida para a lingua do P; str-> str""" 
    string=''
    
    for letra in palavra:
        if letra in 'AEIOUaeiouáãéíóú':
            string+=letra+'p'+letra
        else:
            string+=letra
    return  string