def hashtag(s):
    ''' Dando como entrada uma string s (colocada entre aspas simples 
    ou duplas), a funcao retorna a mesma string, porem com uma # no inicio, no
    meio e no final dela;
    
         Exemplos
    - entrada 'abcd' e saida '#ab#cd#'
    - entrada 'abcde' e saida '#ab#cde#'
    
    Ou seja, caso a string tenha um numero impar de elementos, a # sera colo-
    cada dentro dela logo apos o ultimo caractere de posicao par, de for-
    ma que o elemento 'do meio' (impar) da string original apareca logo apos 
    a # do meio;
    
    str -> str '''
    
    return '#' + s[0:len(s)//2] + '#' + s[len(s)//2:] + '#'