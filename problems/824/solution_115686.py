def uppCons(lista):
   """dado uma frase, retorna essa mesma frase com todas as suas 
   consoantes em maiúsculo e os demais da mesma forma que antes estava
   list, int --> str"""
   i=0
   frase2=[]
   while i < len(frase):
        if str.lower(frase[i]) in "bcdfghjklmnpqrstvxywzç":
            list.append(frase2, str.upper(frase[i]))
        else:
            list.append(frase2, frase[i])
        i = i + 1
    return str.join("", frase2)