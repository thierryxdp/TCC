def inverte(s):
    """Recebe uma frase e retona outra frase com as mesmas palavras, 
    mas em ordem inversa e sem pontuação ou letras maiúsculas.
    assinatura: string --> string
    testes:
    inverte('Eu estudo na UFRJ! Curso Bacharelado em Química...') == 'química em bacharelado curso ufrj na estudo eu'
    inverte('Me chamo Estela. Amo química! Moro em São paulo... Estudo no Rio!') == 'rio no estudo paulo são em moro química amo estela chamo me'
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