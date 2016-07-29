PHOTOS=photo-1-1.jpg photo-2-1.jpg photo-2-2.jpg photo-1.jpg

all: $(PHOTOS)

photo-1-1.jpg:
	convert -size 256x256  xc:\#84e6d2 -pointsize 14 -fill white -stroke black -strokewidth 4 -draw "text 96,128 'photo-1-1'" -stroke none -draw "text 96,128 'photo-1-1'" -bordercolor white -border 8x8 $@

photo-2-1.jpg:
	convert -size 256x256  xc:\#b2c8e6 -pointsize 14 -fill white -stroke black -strokewidth 4 -draw "text 96,128 'photo-2-1'" -stroke none -draw "text 96,128 'photo-2-1'" -bordercolor white -border 8x8 $@

photo-2-2.jpg:
	convert -size 256x256  xc:\#a6f8e0 -pointsize 14 -fill white -stroke black -strokewidth 4 -draw "text 96,128 'photo-2-2'" -stroke none -draw "text 96,128 'photo-2-2'" -bordercolor white -border 8x8 $@

photo-1.jpg:
	convert -size 256x256  xc:\#b6b284 -pointsize 14 -fill white -stroke black -strokewidth 4 -draw "text 96,128 'photo-1'" -stroke none -draw "text 96,128 'photo-1'" -bordercolor white -border 8x8 $@

clean:
	rm -f $(PHOTOS)

.PHONY: clean
