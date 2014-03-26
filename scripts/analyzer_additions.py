def gen_confusion_matrix(my_analyzer, pred_insts, output = None):
    '''
    :func:`gen_confusion_matrix` generates a confusion matrix of a group of
    predicted instances *pred_insts*. If *output* is specified by a path 
    to a file, the result will be outputted to the file instead of  
    on the screen.

            >>> from libshorttext.analyzer import *
            >>> analyzer = Analyzer('model_path')
            >>> insts = InstanceSet('prediction_result_path')
            >>> insts = insts.select(with_labels(['Books', 'Music', 'Art']))
            >>> analyzer.gen_confusion_table(insts)
                     Books  Music  Art
            Books      169      1    0
            Music        2    214    0
            Art          6      0  162
    '''
    if isinstance(output, str):
            output = open(output, 'w')
    if pred_insts.quantity is None:
            my_analyzer._calculate_info(pred_insts)
    labels = pred_insts.true_labels.union(pred_insts.predict_labels)
    #columns = rows
            
    invalid_labels = []
    for label in labels:
            if label not in pred_insts.true_labels and label not in pred_insts.predict_labels:
                    invalid_labels.append(label)
    if invalid_labels:
            invalid_labels = ' '.join(invalid_labels)
            raise Exception('Lables {0} are invalid.'.format(invalid_labels))

    labels_dic = dict(zip(labels, xrange(len(labels))))
    confusion_table = [[0 for i in range(len(labels_dic))] for j in range(len(labels_dic))]
    for inst in pred_insts.insts:
            if inst.true_y in labels_dic and inst.predicted_y in labels_dic:
                    confusion_table[labels_dic[inst.true_y]][labels_dic[inst.predicted_y]] += 1
    for idx_row, row in enumerate(confusion_table):
            for idx_col, col in enumerate(row):
                    confusion_table[idx_row][idx_col] = confusion_table[idx_row][idx_col]
    return (labels, confusion_table)
