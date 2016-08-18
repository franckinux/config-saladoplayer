CUBE_FACES=face_f.tif face_r.tif face_b.tif face_l.tif face_u.tif face_d.tif
CUBE_DIRECTORIES=face_f face_r face_b face_l face_u face_d
CUBE_XML=$(CUBE_DIRECTORIES:=.xml)

all: cube_directories

cubes: $(CUBE_FACES)

face_f.tif:
	convert -size 2048x2048  xc:\#fe8282 -font FreeSans -pointsize 256 -gravity center -fill white -stroke black -strokewidth 5 -draw "text 0,0 'front'" $@

face_r.tif:
	convert -size 2048x2048  xc:\#ee82f2 -font FreeSans -pointsize 256 -gravity center -fill white -stroke black -strokewidth 5 -draw "text 0,0 'right'" $@

face_b.tif:
	convert -size 2048x2048  xc:\#e8f880 -font FreeSans -pointsize 256 -gravity center -fill white -stroke black -strokewidth 5 -draw "text 0,0 'back'" $@

face_l.tif:
	convert -size 2048x2048  xc:\#c0f0d6 -font FreeSans -pointsize 256 -gravity center -fill white -stroke black -strokewidth 5 -draw "text 0,0 'left'" $@

face_u.tif:
	convert -size 2048x2048  xc:\#d4c8e8 -font FreeSans -pointsize 256 -gravity center -fill white -stroke black -strokewidth 5 -draw "text 0,0 'up'" $@

face_d.tif:
	convert -size 2048x2048  xc:\#d2f4c8 -font FreeSans -pointsize 256 -gravity center -fill white -stroke black -strokewidth 5 -draw "text 0,0 'down'" $@

cube_directories: $(CUBE_DIRECTORIES)

face_f: face_f.tif
face_r: face_r.tif
face_b: face_b.tif
face_l: face_l.tif
face_u: face_u.tif
face_d: face_d.tif

$(CUBE_DIRECTORIES):
	vips dzsave $< $@ --tile-size 128 --vips-leak
	mv $@.dzi $@.xml
	sed -e "s/UTF/utf/" -e "s/2008/2009/" -e "s/xmlns/xmnls/" -e "s/></>\n</g" -i $@.xml
	mv $@_files $@

clean:
	rm -f $(CUBE_FACES) $(CUBE_XML)
	rm -rf $(CUBE_DIRECTORIES)

.PHONY: all clean

