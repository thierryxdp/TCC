def  lingua_p ( palavra ):
    #receba como parâmetro uma palavra (em português) e os rendimentos esta mesma palavra projetada: sring => string#
    d  =  1
    palavra  =  palavra . mais baixo ()
    palavra_p  =  lista ( palavra )
    for  i  in  range ( 0 , len ( palavra )):
        if (( palavra [ i ] não  em  'bcdfghjklmnpqrstvwxyz' )):
            palavra_p . insert ( i + d , 'p' + palavra [ i ])
            d  +=  1
    palavra_p  =  '' . juntar ( palavra_p )
    retornar  palavra_p