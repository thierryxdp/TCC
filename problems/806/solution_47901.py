def colisao(xe,xd,ye,yd):

    if ye<xe<yd or ye<xd<yd or xe<ye<xd or xe<yd<xd:

        return true

    else:

        return false