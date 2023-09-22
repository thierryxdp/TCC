#7
#Língua do P
def  lingua_p ( palavra ):
    #receba como parâmetro uma palavra (em português) e os rendimentos esta mesma palavra projetada: sring => string#
    d  =  1
    palavra  =  palavra . inferior ()
    palavra_p  =  lista ( palavra )
    for  i  in  range ( 0 , len ( palavra )):
        if (( palavra [ i ] not  in  'bcdfghjklmnpqrstvwxyz' )):
            palavra_p . insert ( i + d , 'p' + palavra [ i ])
            d  +=  1
    palavra_p  =  '' . join ( palavra_p )
    retornar  palavra_p