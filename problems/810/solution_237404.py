def inverter(frase):
frase=frase.replace('-',' ')
frase=frase.replace(',',' ')
frase=frase.replace(':',' ')
frase=frase.replace(';',' ')
frase=frase.replace('.',' ')
frase=frase.replace('!',' ')
frase=frase.replace('?',' ')
frase=str.lower(frase)
frase=str.split(frase)
frase[::-1]
frase=' '.join(frase)
return frase