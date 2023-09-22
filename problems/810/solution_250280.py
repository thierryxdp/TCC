def inverte(s):
    """Recebe uma frase e retona outra frase com as mesmas palavras, 
    mas em ordem inversa e sem pontuação ou letras maiúsculas.
    assinatura: string --> string
    testes:
    inverte('Moro em Recife! Estudo na Ufrj...') == 'ufrj na estudo recife em moro'
    inverte('Sou de Recife. Capital de Pernambuco! Curso Química...  Estudo na UFRJ!') == 'ufrj na estudo química curso pernambuco de capital recife de sou'
    """
    str.replace(s,".", ' ')
    s2 = str.replace(s,".", ' ')
    str.replace(s2,"!", ' ')
    s3 = str.replace(s2,"!", ' ')
    str.replace(s3,"?",' ')
    s4 = str.replace(s3,"?", ' ')
    str.replace(s4,"-", ' ')
    s5 = str.replace(s4,"-", ' ')
    str.replace(s5,",", ' ')
    s6 = str.replace(s5,",", ' ')
    str.replace(s6,";",' ')
    s7 = str.replace(s6,";", ' ')
    str.replace(s7,"...", ' ')
    s8 = str.replace(s7,"...", ' ')
    str.replace(s8,":", ' ')
    s9 = str.replace(s8,":", ' ')
    str.split(s9)
    ls = str.split(s9)
    list.reverse(ls)
    str.join(" ",ls)
    ls2 = str.join(" ",ls)
    return str.lower(ls2)