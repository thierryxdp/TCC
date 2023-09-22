def uppCons(frase):
    
    posicao=0
    consoante=' '
    
    while posicao<len(frase):
        if frase[posicao] not in 'AEIOUaãâeiíoóuúBCDFGHJLKMNOPQRSTUVXZW':
            frase= str.replace(frase,frase[posicao],str.upper(frase[posicao]))
        posicao=posicao+1
    
    return frase