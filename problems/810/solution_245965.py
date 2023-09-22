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
def inverte(f):
    """Essa função inverte a posição das palavras na frase parâmetro.
       str -> str
       Explicação: Além de inverter as palavras, a função também remove as pontuações
       utilizando a função antes definida 'retira_pontuacao' e também devolve a frase
       com todas as letras minúsculas."""
    rp = retira_pontuacao(f)
    l = str.split(rp)
    i = l[::-1]
    s = str.lower(str.join(' ', i))
    return s
#Teste 1:
#inverte('Nossa, como eu gosto de chocolate.')--> 'chocolate de gosto eu como nossa'

#Teste 2:
#inverte('Pânico! Desespero! Angústia! Mais pânico! Mais desespero!')--> 'desespero mais pânico mais angústia desespero pânico'

#Teste 3:
#inverte('Percebe, Ivair, a petulância do cavalo?')--> 'cavalo do petulância a ivair percebe'