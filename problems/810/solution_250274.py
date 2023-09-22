def inverte(f):
    """ dada uma frase , a função retorna seu 
    inverso"
    assinatura: str --> str
    testes:
    inverte(Nossa,como eu gosto de chocolate)
    == "chocolate de gosto eu como nossa"
    inverte("Deus , está com você")
    == você com está deus
    inverte(Avante Soldados!)
    == soldados avante.
    """
    str.replace(f,".", ' ')
    f2 = str.replace(f,".", ' ')
    str.replace(f2,"!", ' ')
    f3 = str.replace(f2,"!", ' ')
    str.replace(f3,"?",' ')
    f4 = str.replace(f3,"?", ' ')
    str.replace(f4,"-", ' ')
    f5 = str.replace(f4,"-", ' ')
    str.replace(f5,",", ' ')
    f6 = str.replace(f5,",", ' ')
    str.replace(f6,";",' ')
    f7 = str.replace(f6,";", ' ')
    str.replace(f7,"...", ' ')
    f8 = str.replace(f7,"...", ' ')
    str.replace(f8,":", ' ')
    f9 = str.replace(f8,":", ' ')
    str.split(f9)
    ls = str.split(f9)
    list.reverse(ls)
    str.join(" ",ls)
    ls2 = str.join(" ",ls)
    return str.lower(ls2)