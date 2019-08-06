all: data/zaza.html data/wiki.txt fst/diq.gen.hfst


fst/diq.gen.hfst: fst/diq.lexc.hfst fst/diq.twol.hfst
	hfst-compose-intersect -1 fst/diq.lexc.hfst -2 fst/diq.twol.hfst -o fst/diq.gen.hfst

fst/diq.lexc.hfst: fst/diq.lexc
	hfst-lexc fst/diq.lexc -o fst/diq.lexc.hfst

fst/diq.twol.hfst: fst/diq.twol
	hfst-twolc fst/diq.twol -o fst/diq.twol.hfst

data/zaza.html:
	python3 src/bootstrap.py get_dictionary

data/wiki.txt: src/WikiExtractor.py data/wiki.bz2
	python3 src/WikiExtractor.py --infn data/wiki.bz2
	@mv wiki.txt data/

data/wiki.bz2:
	curl https://dumps.wikimedia.org/diqwiki/20190701/diqwiki-20190701-pages-articles-multistream.xml.bz2 --output data/wiki.bz2

src/WikiExtractor.py:
	curl https://svn.code.sf.net/p/apertium/svn/trunk/apertium-tools/WikiExtractor.py > src/WikiExtractor.py
