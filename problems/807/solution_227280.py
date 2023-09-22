def conta_frases(frase):
    '''
    	Funcao que conta o numero de frases que aparecem no texto informado.
        Obs:Cada frase no texto é terminada com um ponto final, um ponto de exclamacao,
        um ponto de interrogacao ou tres pontos em sequencia (reticencias).
        string --> int
    '''
#Exclamação
    frase = str.split(frase, '!')
    frase = str.join(".", frase)
#Interrogação
    frase = str.split(frase, '?')
    frase = str.join(".", frase)
#Ponto final
    frase = str.split(frase, '.')
    frase = str.join(".", frase)
#Reticências
    frase = str.split(frase, '...')
    frase = str.join(".", frase)
#Separação
    frase = str.split(frase,'.')
#Removendo os espaços vazios da lista. 
    frase.remove('')
#contador
    num = len(frase)
    return num