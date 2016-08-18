PHOTOS=photo-1-1.jpg photo-2-1.jpg photo-2-2.jpg photo-1.jpg

all: $(PHOTOS)

photo-1-1.jpg:
	convert -size 256x256  xc:\#84e6d2 -font FreeSans -pointsize 32 -gravity center -draw "text 0,0 'photo-1.1'" -bordercolor white -border 8x8 $@

photo-2-1.jpg:
	convert -size 256x256  xc:\#b2c8e6 -font FreeSans -pointsize 32 -gravity center -draw "text 0,0 'photo-2.1'" -bordercolor white -border 8x8 $@

photo-2-2.jpg:
	convert -size 256x256  xc:\#a6f8e0 -font FreeSans -pointsize 32 -gravity center -draw "text 0,0 'photo-1.1'" -bordercolor white -border 8x8 $@

photo-1.jpg:
	convert -size 256x256  xc:\#b6b284 -font FreeSans -pointsize 32 -gravity center -draw "text 0,0 'photo-1'" -bordercolor white -border 8x8 $@

clean:
	rm -f $(PHOTOS)

.PHONY: all clean
