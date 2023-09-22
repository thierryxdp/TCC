def Convert(string):
      list1=[]
      list1[:0]=string

def uppCons(frase):
    vogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    f1 = Convert(frase)
    c = 0
    while c > len(f1):
      if f1[c] not in vogais:
        f1[c].upper()
      c += 1
    return f1