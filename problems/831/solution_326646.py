def lingua_p(palavra):
    palavra.lower()
    vogal='aâáàãäeêéèëiìíîïoõóòôöuüúùû'
    i=0
    string=str()
    for letra in palavra:
        palavra[i]=palavra[i] + 'p' + palavra[i]
        i+=1
    return palavra