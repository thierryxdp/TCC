def lingua_p(palavra):
    palavra2=''
    for caractere in palavra:
        if caractere in 'aáeéiouAÁEÉIOU':
            palavra2=palavra2+caractere+'p'
        palavra2=palavra2+caractere
    return str.lower(palavra2)
    
lingua_p('Exemplo')