DIRS = $(wildcard pano*/)
TARGETS = $(addsuffix config.xml, $(DIRS))

all: $(TARGETS)

%/config.xml: %/config.py
	python3 ../make-config.py -c config.ini $< > $@

clean:
	rm -f $(TARGETS)

.PHONY: clean
