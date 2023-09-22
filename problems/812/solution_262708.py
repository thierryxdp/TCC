def retira_pontuacao(f):
    """A função acima retorna a str f com todas as suas pontuações substituidas por espaço.
       str -> str"""
    f = str.replace(f, '-', ' ')
    f = str.replace(f, ',', ' ')
    f = str.replace(f, ':', ' ')
    f = str.replace(f, ';', ' ')
    f = str.replace(f, '.', ' ')
    f = str.replace(f, '!', ' ')
    f = str.replace(f, '?', ' ')
    f = str.replace(f, '...', ' ')
    return f
#Teste 1:
#retira_pontuacao('Quem corre, cansa. Quem anda, alcança.')--> 'Quem corre  cansa  Quem anda  alcança '

#Teste 2:
#retira_pontuacao('Bem-te-vi!')--> 'Bem te vi '

#Teste 3:
#retira_pontuacao('Ablublublé? Ablublublé!')--> 'Ablublublé  Ablublublé '