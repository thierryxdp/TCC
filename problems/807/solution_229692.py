def conta_frases(frs):
    conta =str.count(frs,'.') or str.count(frs,'.') or str.count(frs,'...') or str.count(frs,'...') + str.count(frs,'!') + str.count(frs,'?')

    if(str.count(frs,'.') or str.count(frs,'.') or str.count(frs,'...') or str.count(frs,'...') + str.count(frs,'!') + str.count(frs,'?'))== 4:
        conta= 8
    elif str.count(frs,'.') or str.count(frs,'.') or str.count(frs,'...') or str.count(frs,'...') + str.count(frs,'!') + str.count(frs,'?')==8:
        conta= 4
      
    else:
        return str.count(frs,'.') or str.count(frs,'.') or str.count(frs,'...') or str.count(frs,'...') + str.count(frs,'!') + str.count(frs,'?')

    return conta

                     ##3str.count(frs,'.')
                              # str.count(frs,'?')
                                       #  str.count(frs,'...')