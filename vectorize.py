import os
import numpy as np
import gensim
import argparse

parser = argparse.ArgumentParser(description="Vectorize metadata files")

parser.add_argument("metadata", metavar="file", type=str, nargs="+",
        help="A metadata file");

args = parser.parse_args()

print(args.metadata)

data=[]
label=[]
for line in open(path):
    temp=line.split("\t");
    label.append(temp[0])
    data.append(temp[1])
