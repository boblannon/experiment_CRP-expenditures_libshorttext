import csv
import unicodedata

from libshorttext.classifier import TextModel
from libshorttext.classifier import predict_single_text

unlabeled_data_filename = 'data/unlabeled/descrip.unlabeled.csv'
model_filename = 'models/descrip.labeled.csv.svm.model'

mod = TextModel(model_filename)
_dialect = csv.Sniffer().sniff(open(unlabeled_data_filename).readline(100))
_dialect.escapechar = '\\'
data = csv.DictReader(open(unlabeled_data_filename), dialect=_dialect)

out = csv.DictWriter(open('results/descrip.unlabeled.results.csv','w'),
        fieldnames=data.fieldnames+['guess'], dialect=_dialect)

out.writeheader()

for d in data:
    if d['descrip']:
        descrip = d['descrip']
    else:
        descrip = ''
    try:
        descrip = str(descrip)
    except UnicodeEncodeError:
        descrip = descrip.decode('utf-8').encode('ascii','ignore')
    r = predict_single_text(descrip,mod)
    d['guess'] = r.predicted_y
    out.writerow(d)

