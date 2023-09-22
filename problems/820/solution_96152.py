def posLetra(texto,letra,num_oc):
    """Função que fornece o índice(posição) de uma letra em uma certa ocorrência
       na frase mencionada como argumento
       str,str,int ~> int"""
    contador = 0 
    soma = 0
    letraaparece = 0
    if str.count(texto,letra) < num_oc:
        return -1
    else:
        while letraaparece < num_oc:
            if texto[contador] == letra:
                letraaparece += 1 
            contador += 1
    return contador - 1