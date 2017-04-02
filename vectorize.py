import os
import numpy as np
from gensim.models.doc2vec import TaggedDocument
from gensim.models import Doc2Vec
import argparse
import random

parser = argparse.ArgumentParser(description="Vectorize metadata files")

parser.add_argument("metadata", metavar="file", type=str, nargs="+",
        help="A metadata file");

args = parser.parse_args()

files = args.metadata

tags = []
for f in files:
    print("Reading " + f)
    for line in open(f):
        components = line.split("\t")
        tags.append(TaggedDocument(components[2].split(), [components[0]]))

#Randomize document order first
print("Randomizing document order")
random.shuffle(tags)

print("Building model")
model_dm = Doc2Vec(documents=tags, alpha=0.025, size=100, workers=4, dbow_words=1, iter=100, min_count=2)

for i in range(10):
    print("Pass {}".format(i))
    random.shuffle(tags)
    model_dm.train(tags)
    model_dm.alpha -= 0.002
    model_dm.min_alpha = model_dm.alpha

print("Writing word2vec format: wordvectors.txt")
model_dm.wv.save_word2vec_format("wordvectors.txt")

print("Writing doc2vec format: docvectors.txt")
model_dm.save("docvectors.txt")

print("Done")
