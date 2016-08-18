# -*- coding: utf-8 -*-

from model import Panorama, Photo, Tour
from model import GalleryHotspot, InformationHotspot, PanoramaHotspot
from model import PhotoHotspot

# --- photos

photo_1_1 = Photo(
    title="Photo 1",
    path="media/photo-1-1.jpg"
)

photo_2_1 = Photo(
    title="Photo 1",
    path="media/photo-2-1.jpg"
)

photo_2_2 = Photo(
    title="Photo 2",
    path="media/photo-2-2.jpg"
)

photo_nadir = Photo(
    title="Nadir photo",
    path="media/nadir.png"
)

# --- photo hotspots

photo_hotspot_1_1 = PhotoHotspot(
    photo=photo_1_1,
    pan=11,
    tilt=22
)

# --- gallery hotspots

gallery_hotspot_2_1 = GalleryHotspot(
    title="Gallery",
    pan=-10,
    tilt=20,
    photos=[photo_2_1, photo_2_2]
)

# --- information hotspot

information_hotspot_1_1 = InformationHotspot(
    title="This is an information hotspot",
    pan=-9,
    tilt=23
)

# --- panoramas

panorama_1 = Panorama(
    directory="tiles_1",
    title="Panorama 1",
    information_hotspots=[information_hotspot_1_1],
    photo_hotspots=[photo_hotspot_1_1]
)

panorama_2 = Panorama(
    directory="tiles_2",
    title="Panorama 2",
    gallery_hotspots=[gallery_hotspot_2_1],
)

# --- panorama hotspots

panorama_hotspot_1_2 = PanoramaHotspot(panorama=panorama_2, pan=30, tilt=5, show_information=True)
panorama_hotspot_2_1 = PanoramaHotspot(panorama=panorama_1, pan=30, tilt=5, show_information=True)

panorama_1.panorama_hotspots.append(panorama_hotspot_1_2)
panorama_2.panorama_hotspots.append(panorama_hotspot_2_1)

# --- tour

tour = Tour(
    title="Tour exemple",
    first_panorama=panorama_2,
    panoramas=[panorama_1, panorama_2],
    nadir=photo_nadir
)
