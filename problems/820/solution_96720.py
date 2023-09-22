def posLetra(frase,letra,posicao):
    """ Essa função retorna a posição da letra recebida
    no argumento da função. str,str,int->int"""
    lugar = str.find(frase, letra)
    lugar2 = lugar
    primeiro = 1 if not primeiro == -1 else 0
    letra2 = primeiro
    while primeiro and letra2 < posicao:
        lugar2 = lugar
        lugar = str.find(frase, letra, lugar + 1, len(frase) - 1)
        primeiro = 1 if not lugar == -1 else 0
        letra2 += primeiro
    return primeiro