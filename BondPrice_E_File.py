

def getBondPrice_E(face, couponRate, m, yc):
    
    pvcfsum = 0
    cf = face * couponRate
    
    for index,v in enumerate(yc):
        pv = (1 + v)**(-(index + 1))
        pvcf = pv * cf
        pvcfsum = pvcfsum + pvcf
    
    pvcfsum = pvcfsum + face * pv
    return pvcfsum

