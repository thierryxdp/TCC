def media_matriz(s):
   '''funçao que dada uma matriz de
   inteiros não vazia, retorna a média de
   todos os números
   da matriz.
   list->int'''
   n=0
    for i in range(len (s)):
    for j in range (len(s[i])):
        n=n+s[i][j]
        media=n/(len(s)*len(s[0]))
    return round(media,2)