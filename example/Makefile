DIRS = $(wildcard tour*/)
CONFIGS = $(addsuffix config.xml, $(DIRS))

all: install

config: $(CONFIGS)

%/config.xml: %/config.py
	python3 ../make-config.py -c config.ini $< > $@

cube_directories:
	make -C pano all

photos_:
	make -C photos all

install: config cube_directories photos_
	make -C saladoplayer download
	cp -R saladoplayer/static .
	#---
	mkdir static/flash
	mv static/SaladoPlayer-1.3.5.swf static/flash
	cp flash/* static/flash
	#---
	cp javascript/* static/javascript
	#---
	mkdir static/images
	cp -R images/* static/images
	#---
	mkdir tour1/media
	# ln -sf images/nadir-franck-barbenoire.png tour1/media/nadir.png
	# ln -sf photos/photo-1-1.jpg tour1/media
	# ln -sf photos/photo-2-1.jpg tour1/media
	# ln -sf photos/photo-2-2.jpg tour1/media
	cp images/nadir-franck-barbenoire.png tour1/media/nadir.png
	cp photos/photo-1-1.jpg tour1/media
	cp photos/photo-2-1.jpg tour1/media
	cp photos/photo-2-2.jpg tour1/media
	mkdir tour2/media
	cp images/nadir-franck-barbenoire.png tour2/media/nadir.png
	cp photos/photo-1.jpg tour2/media
	#---
	# ln -sf pano tour1/tiles_1
	# ln -sf pano tour1/tiles_2
	# ln -sf pano tour2/tiles_1
	# ln -sf pano tour2/tiles_2
	# ln -sf pano tour2/tiles_3
	cp -r pano tour1/tiles_1
	cp -r pano tour1/tiles_2
	cp -r pano tour2/tiles_1
	cp -r pano tour2/tiles_2
	cp -r pano tour2/tiles_3

serve:
	python3 -m http.server

clean:
	rm -f $(CONFIGS)
	rm -rf static
	make -C pano $@
	make -C photos $@
	make -C saladoplayer $@
	#---
	rm -rf tour1/tiles_1
	rm -rf tour1/tiles_2
	rm -rf tour1/media
	rm -rf tour2/tiles_1
	rm -rf tour2/tiles_2
	rm -rf tour2/tiles_3
	rm -rf tour2/media

.PHONY: all clean install serve
