def uppCons(frase):
    cont=0
    frase.lower()
    frase_nova=[]
     while cont<len(frase):
        if frase[cont] in 'bcdfghjlmnpqrstvxz':
            frase_nova=frase_nova + [frase[cont].upper()
        else:    
            frase_nova=frase_nova + [frase[cont]]                       
          cont=cont +1
     frase_nova=".join(frase_nova)                                
     return frase