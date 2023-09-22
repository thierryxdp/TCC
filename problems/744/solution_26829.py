def hashtag(string):
    '''função que recebe uma string e insira o caractere ”#” no in ıcio, no meio
    e no final dela. Por exemplo, se a entrada for ”abcd”, a saída deve ser ”#ab#cd#”.
    Outro exemplo: se receber ”abcde”, a funç̃ao deve retornar ”#ab#cde#”
    str-> str.'''
    metade=len(string)//2
    primeiraMetade=string[0:metade]
    segundaMetade=string[metade:]
    if len(string)%2==0:
        return str('#')+primeiraMetade+str('#')+segundaMetade+str('#')
    else:
        return str('#')+primeiraMetade+str('#')+segundaMetade+str('#')