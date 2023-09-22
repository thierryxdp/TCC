def inverte(s):
    """recebe uma frase e retorna outra que contenha as mesmas palavras na ordem inversa,sem letras maiùsculas e sem pontuação;str->str"""
    l=str(str.lower(s))
    l1=str(str.replace(l,"!"," "))
    l2=str(str.replace(l1,"?"," "))
    l3=str(str.replace(l2,"."," "))
    l4=str(str.replace(l3,","," "))
    l5=str(str.replace(l4,";"," "))
    l6=str(str.replace(l5,"-"," "))
    l7=str(str.replace(l6,":"," "))
    l8=str(str.split(l7))
    l9=str(l8[::-1])
    l10=str(l9)
    return str(l10[0:-1:1])