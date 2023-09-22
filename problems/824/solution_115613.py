def uppCons(frase):
    '''função que recbe uma frase e retorna todas as consoantes
    em maiúsculo
    valor de entrada: str
    valor de saída: str'''
    i=0
    frasemudada=[]
    while i< len(frase):
        if str.lower(frase[i]) not in 'aeiouãáàeêíóú':
            list.append(frasemudada,str.upper(frase[i]))
        else:
            frasemudada.append(frase[i])
        i= i+1
    return str.join('',frasemudada)