SOURCENAME=slides.tex

all: common/logo.pdf
	pdflatex -shell-escape $(SOURCENAME) 
                                                                                                                                                        

%.pdf: %.svg
	inkscape -D -A $@ $<

%.pdf: %.eps
	epstopdf --outfile=$@ $^

%.eps: %.dia
	dia -e $@ -t eps $^


clean:
	$(RM) -r common/*.pdf *.pdf *.pyg *.snm *.toc *.vrb *.aux *.nav *.out *.dia~ *.log _minted* *.eps $(PICTURES)
