

def getBondPrice_Z(face, couponRate, times, yc):
    pvcfsum = 0
    cf = face * couponRate


    for time, rate in zip(times, yc):
        pv = (1 + rate)**(-(time))
        pvcf = pv * cf
        print(pvcf)
        pvcfsum = pvcfsum + pvcf
    
    pvcfsum = pvcfsum + face * pv
    return pvcfsum

