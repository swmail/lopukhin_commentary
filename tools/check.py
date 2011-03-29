#!/usr/bin/python

def detectOsisId(text):
    i = text.find(' annotateRef="')
    if i >= 0:
        i += 14
        return text[i:text.find('"', i)]
    return ''

# break text line on text portions and xml tags
def textParts(text):
    result = ['']
    text = text.rstrip('\n')
    for i in text:
        if i == '<' and len(result[len(result)-1]) > 0 and result[len(result)-1][0] != '<':
            result.append('')
        result[len(result)-1] += i
        if i == '>' and len(result[len(result)-1]) > 0:
            result.append('')
    if len(result[len(result)-1]) == 0:
        del result[len(result)-1]
    return result

def tagName(tag):
    if tag[0] != '<':
        return ''
    return tag[1:min(tag.find(' '),tag.find('>'))]
    
def checkVerseOrder():
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

def checkTitlesAtEnd():
    osis_in = open('lopukhin_commentary.xml', 'r')
    filter_parts = [').', ')', ')!', '".', ')).', ')".', '),', ']', ',',
                    '.).', '.)', '.].', ').].', '.] .', '. ]', '].', ')?',
                    '"...',
                    #'.', 
                    # TODO following should be inspected
                    ' .', '. ).', ' ', ' ).']

    for l in osis_in:
        osisId = detectOsisId(l)
        if osisId != '':
            ps = textParts(l.decode('utf8'))

            for i in range(len(ps)-1, 0, -1):
                if ps[i][0] != '<' and filter_parts.count(ps[i]) == 0:
                    for ii in range(i, 0, -1):
                        if ps[ii] == '<hi type="bold">' and tagName(ps[ii-1]) != 'div':
                            print osisId, '\ttitle at end:', ps[i-1], ps[i], ps[i+1]
                            break;
                        elif ps[ii][0] != '<':
                            break;
                    break

    osis_in.close()

checkTitlesAtEnd()
