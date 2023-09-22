def retira_pontuacao(s):
    """ função que recebe uma frase e retira
    toda sua pontuação e substitui por espaços.
    assinatura: str --> str
    testes:
    retira_pontuacao( Alemanha , é o maior país)
    ==  ' Alemanha  é o maior país '
    retira_pontuacao
    reira_pontuacao(Ele é muito alto. E também
    é forte)== 'Ele é muito alto E também
    é forte'
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
    return s9