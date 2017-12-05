Super-market frequent item sets
===============================

HOW TO USE
----------

1. clone from git
`git clone https://github.com/imdark/product_co_occurrence.git`
1. make a virtual env with python 3.3
1. run code 'main.py -i retail_25k.dat  -o out.dat'
1. the results will be written to out.dat

TODO
----
1. ~what algorithem to use~:
	1. apriori
	1. Eclat algorithm
	1. FP-growth algorithm

	currently given some experiments FP-growth algorithm seems to run the fastest given the data I tested it with and in general is considered 
	Best of breed in term of memory performance and otherwise

1. pydocs
1. python 3 types
1. clean up
1. ~unit tests~
1. fp_tree pruning
1. move everything to use yield where possible
1. input reading fails


steps to make FP-growth work:
-----------------------------
1. ~make sure it generates all permutations~ looks like working fine
1. ~add frquencies~
1. add conditions for frequencies
1. add limit on set size



References
----------
Han (2000). "Mining Frequent Patterns Without Candidate Generation". Proceedings of the 2000 ACM SIGMOD International Conference on Management of Data. SIGMOD '00: 1–12
https://dl.acm.org/citation.cfm?doid=342009.335372

Comparing Dataset Characteristics that Favor the, Apriori, Eclat or FP-Growth Frequent Itemset, Mining Algorithms
https://arxiv.org/pdf/1701.09042.pdf

The FP-Growth Algorithm variaty of oprimiztion
https://en.wikibooks.org/wiki/Data_Mining_Algorithms_In_R/Frequent_Pattern_Mining/The_FP-Growth_Algorithm

Contains a very good visualiztion of building and usefulness of an FP tree
Apriori and Eclat algorithm in Association Rule Mining
https://www.slideshare.net/wanaezwani/apriori-and-eclat-algorithm-in-association-rule-mining