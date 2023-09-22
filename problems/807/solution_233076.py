def conta_frases(texto):
    '''função responsável por contar o número de frases de um texto, (texto), de escolha do usuário'''
    '''entrada:(texto), um texto da escolha do usuário
    saída: número de frases tendo em mente que os pontos finais marcam o fim de uma frase, podendo assim usá-los de marcação'''
    return str.count(texto,'.') +str.count(texto,'!') +str.count(texto,'?')-2*str.count(texto,'...')