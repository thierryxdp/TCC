def posLetra (string,letra,numero):
    posicao= str.find(string,letra)
    while numero>1:
        posicao=s tr.find(string,leltra,posicao+1)
        numero= numero - 1
    return posicao