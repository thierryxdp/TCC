def inverte(s):
    """Função que dada uma frase, retorna outra frase com todas as palavras com letras minúsculas, escrita ao contrário e sem pontuações.
str -> str
testes:
inverte(""Victor Marinho. Estuda computação... É professor? Um dia vai se formar..."") == 'formar se vai dia um professor é computação estuda marinho victor'
inverte("Você vai à festa? Não tem como, vou precisar estudar...") == 'estudar precisar vou como tem não festa à vai você'
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