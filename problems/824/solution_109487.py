def uppCons(frase):
    '''recebe uma frase e retorna uma frase com todas
    as suas consoantes em maiusculas'''
    
 consoante = ["b","c","d","f","g","h","j","k","l","m",
              "n","p","q","r","s","t","v","w","x","z","ç"]
 
 consoanteM = ["B","C","D","F","G","H","J","K","L","M",
                  "N","P","Q","R","S","T","V","W","X","Z","Ç"]
 
fraselist = []
u = 0
while u < len(frase):
  fraselist.append(frase[u])
  u=u+1
i = 0
a = 0
while i  < len(fraselist):
  if fraselist[i] in conso:
     b = consoante.index(fraselist[i])
     fraselist[i] = consoanteM[b]
  i=i+1
frase = ''.join(fraselist)
return frase