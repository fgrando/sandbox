SOURCENAME=toolsAndTips.tex

# I will add here once I have a proper logo
#all: common/logo.pdf
#	pdflatex -shell-escape $(SOURCENAME)

all: all-debug
	rm *.out *.nav *.log *.snm *.toc *.aux 

all-debug: all
	pdflatex -shell-escape $(SOURCENAME)

%.pdf: %.svg
	inkscape -D -A $@ $<

%.pdf: %.eps
	epstopdf --outfile=$@ $^

%.eps: %.dia
	dia -e $@ -t eps $^


clean:
	$(RM) -r common/*.pdf *.pdf *.pyg *.snm *.toc *.vrb *.aux *.nav *.out *.dia~ *.log _minted* *.eps $(PICTURES)
