CUBE_FACES=face_f.tif face_r.tif face_b.tif face_l.tif face_u.tif face_d.tif
CUBE_DIRECTORIES=face_f face_r face_b face_l face_u face_d
CUBE_XML=$(CUBE_DIRECTORIES:=.xml)

all: cube_directories

cubes: $(CUBE_FACES)

face_f.tif:
	convert -size 1024x1024  xc:\#fe8282 -pointsize 72 -fill white -stroke black -strokewidth 15 -draw "text 400,512 'front'" -stroke none -draw "text 400,512 'front'" $@

face_r.tif:
	convert -size 1024x1024  xc:\#ee82f2 -pointsize 72 -fill white -stroke black -strokewidth 15 -draw "text 400,512 'right'" -stroke none -draw "text 400,512 'right'" $@

face_b.tif:
	convert -size 1024x1024  xc:\#e8f880 -pointsize 72 -fill white -stroke black -strokewidth 15 -draw "text 400,512 'back'" -stroke none -draw "text 400,512 'back'" $@

face_l.tif:
	convert -size 1024x1024  xc:\#c0f0d6 -pointsize 72 -fill white -stroke black -strokewidth 15 -draw "text 400,512 'left'" -stroke none -draw "text 400,512 'left'" $@

face_u.tif:
	convert -size 1024x1024  xc:\#d4c8e8 -pointsize 72 -fill white -stroke black -strokewidth 15 -draw "text 400,512 'up'" -stroke none -draw "text 400,512 'up'" $@

face_d.tif:
	convert -size 1024x1024  xc:\#d2f4c8 -pointsize 72 -fill white -stroke black -strokewidth 15 -draw "text 400,512 'down'" -stroke none -draw "text 400,512 'down'" $@

cube_directories: $(CUBE_DIRECTORIES)

face_f: face_f.tif
face_r: face_r.tif
face_b: face_b.tif
face_l: face_l.tif
face_u: face_u.tif
face_d: face_d.tif

$(CUBE_DIRECTORIES):
	vips dzsave $< $@ --tile-size 512 --vips-leak
	mv $@.dzi $@.xml
	mv $@_files $@

clean:
	rm -f $(CUBE_FACES) $(CUBE_XML)
	rm -rf $(CUBE_DIRECTORIES)

.PHONY: clean

