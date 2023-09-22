def substitui(s,x,i):
    """Função que, ao receber uma string 's', um caracter 'x' e um inteiro 'i', 
    retorna a str s com o termo correspondente ao i substituído pelo termo de x.
       str, str, int -> str"""
    s1 = s[:i]
    s2 = s[i+1:]
    return s1 + x + s2

#Teste 1:
#substitui('Laiza', 'u', 1)--> 'Luiza'

#Teste 2:
#substitui('Py thon', '', 2)--> 'Python'

#Teste 3:
#substitui('Luis', 'z', 3)--> 'Luiz'