# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str, str -> str
def concatenacao(a, b):
    "Função que quando informado duas strings a e b, retorna a junção delas no format abba.
    assinatura - str, str --> str
    testes - 
    concatenacao("sim","nao") == "simnaonaosim"
    concatenacao("oi","tchau") == "oitchautchauoi"
    "
    return (str(a)+str(b)+str(b)+str(a))