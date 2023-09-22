def media(notas):
    '''Função que soma todos os elementos do parâmetro dado e
divide pelo número de elementos dados
    lista -> float'''

    Soma = sum(notas)
    Qtdade = len(notas)
    Media = Soma/Qtdade
    
    return Media

def acima_da_media(notas,media):
    '''Função que dada uma lista de notas de alunos de uma turma retorna
uma lista ordenada com notas que ficaram acima da média.
    lista -> lista'''

	return notas[notas.index(media)+notas.count(media):]