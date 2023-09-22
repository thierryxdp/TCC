def retira_pontuacao(s):
    fpoint = str.replace(s,'...','.')
    tpoint = str.replace(fpoint,'..','.')
    esppoint = str.replace(tpoint,'.',' ')
    esptravess = str.replace(esppoint,'-',' ')
    espvirg = str.replace(esptravess,',',' ')
    esppointvirg = str.replace(espvirg,';',' ')
    espexcl = str.replace(esppointvirg,'!',' ')
    espint = str.replace(espexcl,'?',' ')
    return espint