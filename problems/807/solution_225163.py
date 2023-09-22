def conta_frases(frase):
    """A função 'conta_frases' retorna quantas frases há no texto dado como entrada.
       str -> int
       Explicação: Os delimitadores das frases são os pontos '.', '...', '!', '?'.
       Somente eles finalizam cada frase do texto. Sendo assim, basta contar as
       ocorrências desses pontos para, automaticamente contar a ocorrência de cada
       frase no texto parâmetro.
       Entretanto, substituiremos '...' por '.', pois, caso contrário a função
       contará '...' e '.'. 
       Exemplo: 'Vou perder minha aula...'
       Se não houver a substituiçao, a função contará:
       '.' que imediatamente sucede 'a';
       '.' que sucede o 1º '.';
       '.' que sucede o 2º '.' e
       '...'
       Logo, após essa substituição, poderemos contar as pontuações e retornar a 
       contagem correta."""
    sem_ret = str.replace(frase, '...', '.')
    pFinal = str.count(sem_ret, '.')
    pExc = str.count(frase, '!')
    pInt = str.count(frase, '?')
    total_frases = pFinal + pExc + pInt 
    return total_frases

#Teste 1:
#conta_frases('Preciso tirar um cochilo. Meu Deus! Que horas são? Vou perder minha aula...')--> 4

#Teste 2:
#conta_frases('O que os olhos não veêm o coração não sente.')--> 1

#Teste 3:
#conta_frases('Se percebeste, percebeste. Se não percebeste, faz que percebeste para que eu perceba que tu percebeste. Percebeste?')--> 3