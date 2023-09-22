def posLetra(texto,letra,num_oc):
    """Função que fornece o número da posição de uma letra na frase mencionada
       str,str,int ~> int"""
    contador = 0 
    soma = 0
    letraaparece = 0
    if str.count(texto,letra) < num_oc:
        return -1
    else:
        while letraaparece < num_oc:
            if texto[contator] == letra:
                letraaparece += 1 
            contador += 1
    return contador