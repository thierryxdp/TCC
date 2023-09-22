def hashtag(s):
     """Funcao que receba uma string e insira o
    caractere ”#” no início, no meio e no final dela
    str-> str"""
    return str("#") + str(s[:len(s)//2])+ str("#") +str(s[len(s)//2:])+ str("#")