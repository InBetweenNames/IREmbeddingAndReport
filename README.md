Author: Shane Peelar <peelar@uwindsor.ca>

If you use this program in your project, please cite me.  You can use
this BiBTeX entry:

~~~
@article{peelar, title={Vectorize.py}, url={https://github.com/InBetweenNames/IREmbeddingAndReport}, author={Peelar, Shane M}} 
~~~

~~~
python3 vectorize.py --train icse_id.txt vldb_id.txt sigmod_id.txt  --dumpdocvectors docvecs.txt
~~~

~~~
usage: vectorize.py [-h] [--train file [file ...]] [--model model]
                    [--findsimilar FINDSIMILAR]
                    [--dumpdocvectors DUMPDOCVECTORS]

Vectorize metadata files

optional arguments:
  -h, --help            show this help message and exit
  --train file [file ...]
                        A metadata file
  --model model         Pre-trained doc2vec model (use --train to create)
  --findsimilar FINDSIMILAR
                        Find all documents similar to the listed one
  --dumpdocvectors DUMPDOCVECTORS
                        Dump document vectors to file (requires --train or
                        --model)
~~~
