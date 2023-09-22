def hashtag(s):
    '''
    Funcao que recebe uma string e insere o caratere "#" no início, no meio e no final dela.
	Por exemplo, se a entrada for "abcd", a saída deve ser "#ab#cd#".
	Outro exemplo: se receber "abcde", a saída deve ser "#ab#cde#"
    '''
    return "#" + s[:len(s)//2] + "#" + s[len(s)//2:] + "#"