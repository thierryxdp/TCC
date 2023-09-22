def lingua_p(palavra: str):
    pos=0
    pe=''
    for caractere in palavra:
        if caractere in 'AEIOUaeiou':
            return caractere+p