def lingua_p(palavra):
    palavra.lower()
    vogal='aâáàãäeêéèëiìíîïoõóòôöuüúùû'
    i=0
    for letra in palavra:
        palavra=palavra[i] + 'p' + palavra[i]
        i+=1
    return palavra