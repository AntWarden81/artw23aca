import csv
import time

datafile = 'data.csv'
dateDic, ageDic, raceDic = {}, {}, {}
n = 0
sexDic, wtDic, eyeDic, hairDic, = {}, {}, {}, {}
avgHt = 0
n2 = 0
def read_data(path):
    with open(path, 'rU') as data:
        reader = csv.DictReader(data)
        for row in reader:
            yield row

def avg_data(data):
    total = 0
    n = 0
    for key in data:
        val = key
        if val != '':
            val = int(val)
            total += val
            n += 1
    return total / n

if __name__ == "__main__":
    for idx, row in enumerate(read_data(datafile)):
        if "WARRANT" not in row["Arrest Type"]:
            n += 1
            date = row['Date and Time'][:10]
            race = row['Race']
            sex = row['Sex']
            age = row['Age']
            wt = row['Weight']
            ht = row['Height']
            hair = row['Hair']
            eyes = row['Eyes']
            print date
            if date not in dateDic:
                dateDic[date] = 1
            else:
                dateDic[date] += 1
            if race not in raceDic:
                raceDic[race] = 1
            else:
                raceDic[race] += 1
            if sex not in sexDic:
                sexDic[sex] = 1
            else:
                sexDic[sex] += 1
            if age not in ageDic:
                ageDic[age] = 1
            else:
                ageDic[age] += 1
            if wt not in wtDic:
                wtDic[wt] = 1
            else:
                wtDic[wt] += 1
            if hair not in hairDic:
                hairDic[hair] = 1
            else:
                hairDic[hair] += 1
            if eyes not in eyeDic:
                eyeDic[eyes] = 1
            else:
                eyeDic[eyes] += 1
            if ht != ' ' and ht != '':
                n2 += 1
                avgHt += int(ht[0])
                if len(ht) == 11:
                    avgHt += float(ht[6:7])/float(12)
                if len(ht) == 12:
                    avgHt += float(ht[6:8])/float(12)

newDic = {}
for key in sorted(dateDic.iterkeys()):
    print key, "; ",  dateDic[key]
    newDic[key] = dateDic[key]
print newDic
temp = 0
for date in newDic:
    temp += newDic[date]
print temp
print raceDic
print sexDic
print eyeDic
print hairDic
print "Average Height", avgHt/float(n2)
print "Average Weight: " , avg_data(wtDic)
print "Average Age: " , avg_data(ageDic)
time.sleep(250)

