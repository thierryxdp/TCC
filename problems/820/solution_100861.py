def posLetra(frase,letra,n):
    '''Funcao que, dada uma string (frase), uma letra e um numero (n), retorna em que posicao da string aquela ocorrencia esta; str, str, int -> int''' 
    i=0
    inicio=0
    while i<n:
        inicio+=str.find(frase,letra,inicio)-inicio+1
        i+=1
    return inicio-1