def inverte(s):
    """Recebe uma frase e retona outra frase com as mesmas palavras, 
    mas em ordem inversa e sem pontuação ou letras maiúsculas.
    assinatura: string --> string
    testes:
    inverte('Eu moro na Ilha do Governador! Amo meu bairro...') == 'bairro meu amo governador do ilha na moro eu'
    inverte('Meu apelido é manu. Eu adoro qúimica! Estudo no Fundão!') == 'fundão no estudo qúimica adoro eu manu é apelido meu'
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