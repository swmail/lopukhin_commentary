#!/usr/bin/python

osis_in = open('lopukhin_commentary.xml', 'r')

osisId_prev = '0.0.0'

for l in osis_in:
    # detect osisId
    i = l.find(' annotateRef="')
    if i >= 0:
        i += 14
        osisId_current = l[i:l.find('"', i)]
        osisId = osisId_current

        if osisId.find('-') >= 0:
            osisId = osisId[0:osisId.find('-')]

        osisId = osisId.rstrip('abcd')

        v1 = int(osisId.split('.')[2])
        c1 = int(osisId.split('.')[1])
        b1 = osisId.split('.')[0]

        v2 = int(osisId_prev.split('.')[2])
        c2 = int(osisId_prev.split('.')[1])
        b2 = osisId_prev.split('.')[0]

        if b1 == b2 and c1 == c2 and v2 > v1:
            print 'Wrong annotation order: ', osisId_current

        osisId_prev = osisId

osis_in.close()
