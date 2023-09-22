# str-> str
def hashtag(s):
    '''função que retorna uma string com caractere (#)
    no início, no meio e final dela; str ->str'''
    inicio = s[:len(s)//2]
    final = s[len(s)//2:]
    s = "#" + s[:len(s)//2] + "#" + s[len(s)//2:] + "#"
    return s