# Preparing text training file
import csv
import sys

target = 'Expcode'
text = 'Descrip'

d = csv.Sniffer().sniff(open('expends2012.unix.w-headers.csv').readline(10000))
d.delimiter = ','
d.lineterminator = '\r\n'
d.quotechar =  '|'
d.quoting = csv.QUOTE_ALL
d.skipinitialspace = False

dr = csv.DictReader(open('expends2012.unix.w-headers.csv'),dialect=d)
keep = [target, text]
dw = csv.DictWriter(open('expends2012.all.csv','w'),fieldnames=keep,restval='?',extrasaction='ignore',delimiter='\t')
for row in dr:
    if row[target].replace(' ','').replace('\t','') == '':
        del row[target]
    else:
        row[target] = row[target].upper()
    if row[text].replace(' ','').replace('\t','') == '':
        row[text] = '~NA~'
    dw.writerow(row)
