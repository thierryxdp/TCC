def retira_pontuacao(frase):
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
    return str.replace(frase,',','')