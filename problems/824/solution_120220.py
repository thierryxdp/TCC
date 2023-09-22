def uppCons (texto):
   '''função que retorna consoante maiúscula'''
    cont=0
    texto_m=''
    while cont<len (texto):
        if str.lower(texto[cont]) in 'bcdfghjklmnpqrstvwxyzç':
            texto_m+=str.upper(texto[cont])
            cont+=1
        else:
            texto_m+=texto[cont]
            cont+=1 
    return texto_m