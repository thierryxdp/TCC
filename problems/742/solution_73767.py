def substitui(s ,x , i):
"""Recebe uma string, uma posção na string e um caractere e substitui esse caractere em determinada posição na string
str + int + str -> str"""
a = list(s)
a[i] = x
 return str.join("",a)