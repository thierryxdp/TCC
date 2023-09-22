def inverte(s):
    """recebe uma frase e retorna outra que contenha as mesmas palavras na ordem inversa,sem letras maiùsculas e sem pontuação;str->str"""
    l=str.lower(s)
    l1=str.replace(l,"!"," ")
    l2=str.replace(l1,"?"," ")
    l3=str.replace(l2,"."," ")
    l4=str.replace(l3,","," ")
    l5=str.replace(l4,";"," ")
    l6=str.replace(l5,"-"," ")
    l7=str.replace(l6,":"," ")
    l8=str.split(l7)
    l9=l8[::-1]
    l10=str(l9)
    return str(l10)