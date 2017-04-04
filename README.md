Author: Shane Peelar <peelar@uwindsor.ca>

If you use this program in your project, please cite me.  You can use
this BiBTeX entry:

~~~
@article{peelar, title={Vectorize.py}, url={https://github.com/InBetweenNames/IREmbeddingAndReport}, author={Peelar, Shane M}} 
~~~

~~~
python3 vectorize.py --train icse_id.txt vldb_id.txt sigmod_id.txt  --dumpdocvectors docvecs.txt --dumpwordvectors wordvectors.txt
~~~

Both the document vectors and word vectors are space delimited.

The document vector file has the form, for each paper's corresponding paperid:
~~~
<paperid> <conference> <vector>
~~~

The word vector file has the form, for each unique word in the metadata files:
~~~
<word> <vector>
~~~

To reuse existing training data:

~~~
python3 vectorize.py --model docvectors.model --dumpdocvectors docvecs.txt --dumpwordvectors wordvectors.txt
~~~

~~~
usage: vectorize.py [-h] [--train file [file ...]] [--model model]
                    [--findsimilar FINDSIMILAR]
                    [--dumpdocvectors DUMPDOCVECTORS]
                    [--dumpwordvectors DUMPWORDVECTORS]

Vectorize metadata files

optional arguments:
  -h, --help            show this help message and exit
  --train file [file ...]
                        A metadata file
  --model model         Pre-trained doc2vec model (use --train to create)
  --findsimilar FINDSIMILAR
                        Find all documents similar to the listed one (must
                        include conference name, for example --findsimilar
                        '<id> <conference>', a space character must exist
                        between <id> and <conference>)
  --dumpdocvectors DUMPDOCVECTORS
                        Dump document vectors to file (requires --train or
                        --model)
  --dumpwordvectors DUMPWORDVECTORS
                        Dump word vectors to file (requires --train or
                        --model)

~~~
