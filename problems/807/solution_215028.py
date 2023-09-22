#Mirella Maturo da Cruz DRE:119023985 Questão 2 do Laboratório 5
def conta_frases (texto):
    '''Retorna a contagem do número de frases que aparecem em um texto
    String -> int '''
    numero=texto.count('...')*(-2)
    numero+=texto.count('!')
    numero+=texto.count('?')
    numero+=texto.count('.')
    if numero == 0:
        numero+= 1
        return numero
    else: 
        return numero