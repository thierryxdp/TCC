def uppCons (frase):
    ''' função que ao receber uma frase, retorna uma nova
        frase similar a anterior, porém com todas as
        consoantes alteradas para a versão em maiúsculo
        [string --> string]'''
    
    indice = 0
    
    while indice < len(frase):
        if frase[indice] in 'bcdfghjklmnpqrstvwzBCDFGHJKLMNPQRSTVWXZ':
            frase =str.replace(frase,frase[indice],str.upper(frase[indice]))

        indice += 1

    return frase