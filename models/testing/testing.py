import json
import nltk
from nltk.translate.bleu_score import corpus_bleu
from nltk.translate.meteor_score import meteor_score
import numpy as np

from models.mbart import mbart_translator
from models.helsinki import helsinki_translator
from models.google import googletrans_translator
from models.nllb import nllb_translator

nltk.download('wordnet')

meteor_scores = []
translated = []
references_english = []
which_model = 1

# Bleu
with open('data.json', 'r', encoding='utf-8') as json_file:
    test_data = json.load(json_file)

for n in test_data['translations']:

    if which_model == 0:
        tymczasowe = [googletrans_translator(n['polish'])]
    elif which_model == 1:
        tymczasowe = [mbart_translator(n['polish'])]
    elif which_model == 2:
        tymczasowe = [helsinki_translator(n['polish'])]
    else:
        tymczasowe = [nllb_translator(n['polish'])]
    translated.append(tymczasowe)
    tymczasowe_english = [n['english']]
    references_english.append(tymczasowe_english)


print(translated)
print(references_english)

bleu_scores = [corpus_bleu(reference, machine) for reference, machine in zip(references_english, translated)]
mean_bleu_score = np.mean(bleu_scores)

# Precyzja, Recall i F1
precision_sum = 0.0
recall_sum = 0.0

for reference, candidate in zip(references_english, translated):
    reference_tokens = reference[0].split()
    candidate_tokens = candidate[0].split()
    common_tokens = set(reference_tokens) & set(candidate_tokens)

    precision = len(common_tokens) / len(candidate_tokens)
    recall = len(common_tokens) / len(reference_tokens)
    precision_sum += precision
    recall_sum += recall

    if precision + recall == 0:
        f1 = 0.0
    else:
        f1 = 2 * (precision * recall) / (precision + recall)

average_precision = precision_sum / len(references_english)
average_recall = recall_sum / len(references_english)

# Meteor
for reference, candidate in zip(references_english, translated):
    reference_sentence = reference[0].split()
    candidate_sentence = candidate[0].split()

    meteor = meteor_score([reference_sentence], candidate_sentence)
    meteor_scores.append(meteor)

average_meteor_score = sum(meteor_scores) / len(meteor_scores)

print("BLEU Score: ", mean_bleu_score)
print("METEOR Score: ", average_meteor_score)
print("Średnia precyzja: ", average_precision)
print("Średni recall: ", average_recall)
print("Średnia miara F1: ", (2 * average_precision * average_recall) / (average_precision + average_recall))
