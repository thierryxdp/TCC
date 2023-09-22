def conta_frases(texto):
    '''Funcao que recebe de entrada um texto armazenado em 
    uma string e retorna a quantdidade de frases presentes
    nesse texto. Para uma parte do texto ser considerada
    uma frase, ela precisa terminar com ponto final, ponto de 
    exclamacao, reticencias ou ponto de interrogacao.
    str -> int'''
    texto = str.replace(texto,'...', '.')
    texto = str.replace(texto, '!', '.')
    texto = str.replace(texto, '?', '.')
    return len(str.split(texto,'.'))-1

#conta_frases('Fui no shopping as 14h da tarde. Comprei um pao de queijo e nossa...
# estava delicioso! Depois, fui visitar minha tia e voltei para casa. Que dia longo!') == 5

#conta_frases(' ') == 0

#conta_frases(Dado um texto armazenado em uma string, faca a func˜ao que conte o numero de frases que aparecem
#neste texto. Cada frase no texto e terminada com um ponto final, um ponto de exclamac˜ao um ponto
#de interrogac˜ao ou tres pontos em sequencia (reticencias). Pontos de exclamac˜ao ou de interrogac˜ao n˜ao
#aparecer˜ao repetidos em sequencia no texto e esses sımbolos so aparecem no texto terminando uma frase.
#No exemplo a seguir, s˜ao contadas 4 frases: “Preciso tirar um cochilo. Meus Deus! Que horas s˜ao? Vou
#perder a minha aula...”) = 7 (comando da questão 2)