#adapted from https://thepythoncode.com/article/calculate-word-error-rate-in-python

import numpy as np

def calculate_wer(reference, hypothesis):
    ref_words = reference.split()
    hyp_words = hypothesis.split()
    
    d = np.zeros((len(ref_words) + 1, len(hyp_words) + 1))
    operations = np.empty((len(ref_words) + 1, len(hyp_words) + 1), dtype=object)
    
    for i in range(len(ref_words) + 1):
        d[i, 0] = i
        operations[i, 0] = 'D' if i > 0 else None  
    for j in range(len(hyp_words) + 1):
        d[0, j] = j
        operations[0, j] = 'I' if j > 0 else None  
    
    for i in range(1, len(ref_words) + 1):
        for j in range(1, len(hyp_words) + 1):
            if ref_words[i - 1] == hyp_words[j - 1]:
                d[i, j] = d[i - 1, j - 1]
                operations[i, j] = 'M'  
            else:
                substitution = d[i - 1, j - 1] + 1
                insertion = d[i, j - 1] + 1
                deletion = d[i - 1, j] + 1
                
                min_cost = min(substitution, insertion, deletion)
                d[i, j] = min_cost
                
                if min_cost == substitution:
                    operations[i, j] = 'S'  
                elif min_cost == insertion:
                    operations[i, j] = 'I'  
                else:
                    operations[i, j] = 'D'  
    
    i, j = len(ref_words), len(hyp_words)
    substitutions, insertions, deletions = 0, 0, 0
    while i > 0 or j > 0:
        if operations[i, j] == 'S':
            substitutions += 1
            i -= 1
            j -= 1
        elif operations[i, j] == 'I':
            insertions += 1
            j -= 1
        elif operations[i, j] == 'D':
            deletions += 1
            i -= 1
        else:
            i -= 1
            j -= 1
    
    wer = (substitutions + insertions + deletions) / len(ref_words)
    return wer, substitutions, insertions, deletions