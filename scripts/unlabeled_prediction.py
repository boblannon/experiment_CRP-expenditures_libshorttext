from libshorttext.classifier import TextModel
from libshorttext.classifier import predict_single_text


data = [line.strip().split('\t') for line in open('data/unlabeled/expends2012.description.unlabeled.csv')]
mod = TextModel('models/expends2012.description.sorted-labeled.csv.svm.model')

out = open('results/expends2012.description.unlabeled.results.csv','w')

for d in data:
    r = predict_single_text(d[1],mod)
    out.write('\t'.join([r.predicted_y,d[1]])+'\n')

out.close()
