import os
import numpy as np
from gensim.models.doc2vec import TaggedDocument
from gensim.models import Doc2Vec
import argparse
import random

parser = argparse.ArgumentParser(description="Vectorize metadata files")

parser.add_argument("--train", metavar="file", type=str, nargs="+",
        help="A metadata file");

parser.add_argument("--model", metavar="model", type=str, help="Pre-trained doc2vec model (use --train to create)")

parser.add_argument("-e", "--evaluate", action="store_true", help="Evaluate model (requires --train or --model)")

parser.add_argument("--findsimilar", help="Find all documents similar to the listed one")

args = parser.parse_args()

model_dm = ""

if args.model is not None:
    print("Loading " + args.model)
    model_dm = Doc2Vec.load(args.model)
elif args.train is not None:
    files = args.train

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

    print("Writing doc2vec format: docvectors.model")
    model_dm.save("docvectors.model")

    print("Done")

if args.evaluate and model_dm != "":
    print("Evaluating model")

if args.findsimilar and model_dm != "":
    print("Documents similar to: " + args.findsimilar)
    simdocs = model_dm.docvecs.most_similar(["7EAE63BC"])
    print(simdocs)
