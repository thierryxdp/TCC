"""A função abaixo, como determinado no exercício, fatia uma string qualquer de tal forma que no começo, meio e fim
desta haja uma hashtag (#).
  A mesma utiliza a função len para determinar o número de letras da string e assim separá-la em duas
partes - por isso a divisão por 2 -, enquanto que a função int é responsável por arredondar os valores das divisões dos números ímpares por 2
- caso a palavra posta tenha uma quantidade ímpar de letras."""
def hashtag (palavra):
    return '#' + palavra[0:int(len(palavra)/2)] + '#' + palavra[(int(len(palavra)/2)):len(palavra)] + '#'