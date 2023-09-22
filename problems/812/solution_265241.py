def retira_pontuacao(s):
    """Função que quando informada uma frase, substitua as pontuações presentes por espaços
assinatura: string -> string
testes:
retira_pontuacao("Meu nome, é Maria. Tenho 22 anos! Não sei o que estou fazendo dessa vida, Sofro... por férias? Sim.") == 'Meu nome  é Maria  Tenho 22 anos  Não sei o que estou fazendo dessa vida  Sofro    por férias  Sim '
retira_pontuacao("Olá! senta lá, Cláudia.") == 'Olá  senta lá  Cláudia '
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