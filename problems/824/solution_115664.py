def uppcons(frase):
 contador=0
 letra = 'bcdfghjklmnpqrstvxwyz'
 frase_final = ' '
 while contador < len(frase):
     caractere = frase[contador]
     str.split(frase)
     if caractere in letra:
      caractere = str.upper(caractere)
      frase_final += caractere
      contador += 1

 return (frase)