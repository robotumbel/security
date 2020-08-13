# count alert snort fast

def newfile(baris,namefile):

    file = 'count_'+namefile+'.txt'
    f = open(file,'a')
    f.write(baris+'\n')
    f.close()

def alert(name_alert):

    dect = {}
    file = open(name_alert,'r')
    value = file.read()
    file.close()
    value = value.split('\n')
    for i in range(len(value)):
        if value[i] != '':
            data = value[i].replace('[**]', '')
            data = data.replace('{', '[')
            data = data.replace('}', ']')
            data = data.replace('   ', ' ')
            data = data.split('] [')
            #print(data)
            index1 = data[0].split('] ')
            filed = index1[1].split(' [')
            #print(filed[0],filed[1],data[1])

            if filed[0] not in dect:
                dect[filed[0]]= 1
            else:
                dect[filed[0]]=dect[filed[0]] + 1
    print(dect)
    for k,y in dect.items():
        print(k,y)
        newfile(k+str(y),name_alert)


alert('alert_jumat')