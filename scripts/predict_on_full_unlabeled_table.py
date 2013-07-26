import json

from libshorttext.classifier import TextModel
from libshorttext.classifier import predict_single_text

mod = TextModel('models/expends2012.description.sorted-labeled.csv.svm.model')
data = json.load(open('/home/blannon/og_data/expenditures/expends12-unlabeled-csv.json'))

out = open('results/expends2012.unlabeled.full.results.csv','w')

for d in data['rows']:
    if d['descrip']:
        descrip = str(d['descrip'])
    else:
        descrip = ''
    r = predict_single_text(descrip.encode('ascii','ignore'),mod)
    print d['ID'],descrip,r.predicted_y
    out.write('\t'.join([str(a) for a in [d['ID'],r.predicted_y]]))
    out.write('\n')

out.close()
