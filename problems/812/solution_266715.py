def retira_pontuacao(texto):
    ''' 
    Função recebe um texto e remove caracteres especiais que estão em uma lista pre-definida
    '''
    # usando replace () para remover caracteres especiais
    caracteres_interesse = "@_!'^#$%^&*()<>?/\|}{~:;[],...-"
    for i in caracteres_interesse: 
          texto = texto.replace(i, ' ')
    return texto