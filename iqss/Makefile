TARGET = iqss

all: $(TARGET).pdf

$(TARGET).pdf: $(TARGET).tex *.tex
	xelatex $< && xelatex $<
	make rmtmp

rmtmp:
	rm -vf $(TARGET).out
	rm -vf $(TARGET).toc
	rm -vf $(TARGET).aux
	rm -vf $(TARGET).log
	rm -vf $(TARGET).nav
	rm -vf $(TARGET).vrb
	rm -vf $(TARGET).snm

clean:
	rm -vf $(TARGET).pdf
	make rmtmp

