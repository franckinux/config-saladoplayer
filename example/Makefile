DIRS = $(wildcard tour*/)
CONFIGS = $(addsuffix config.xml, $(DIRS))

all: config cube_directories photos_

config: $(CONFIGS)

%/config.xml: %/config.py
	python3 ../make-config.py -c config.ini $< > $@

cube_directories:
	make -C pano all

photos_:
	make -C photos all

clean:
	rm -f $(CONFIGS)
	make -C pano $@
	make -C photos $@

.PHONY: clean
