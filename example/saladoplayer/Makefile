all: download

download:
	wget -nc -q http://transferts.franck-barbenoire.fr/saladoplayer/SaladoPlayer_binaries-1.3.5.tar.gz
	mkdir static
	tar xzf SaladoPlayer_binaries-1.3.5.tar.gz -C static

clean:
	rm -rf static
	rm  -f SaladoPlayer_binaries-1.3.5.tar.gz

.PHONY: all clean download
