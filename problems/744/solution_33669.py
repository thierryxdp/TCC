# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Dada uma string /s/, retorna /s/ intercalado com /#/. 
    Sendo que deve ter /#/ no começo, meio e fim no seguinte 
    modelo:
    Se /s/ é "abcd", a função deve retornar "#ab#cd#". Em 
    strings maiores como "abcde", a função deve retornar 
    "#ab#cde#"
    assinatura: str --> str
    testes:
    hashtag('abcd') == '#ab#cd#'
    hashtag('abcde') == '#ab#cde#'
    hashtag('estela') == '#es#tela#'
    """
    return str('#') + s[0:2] + str('#') + s[2:] + str('#')