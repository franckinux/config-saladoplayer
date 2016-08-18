# -*- coding: utf-8 -*-

from model import Panorama, Photo, Tour
from model import InformationHotspot, PanoramaHotspot
from model import PhotoHotspot, LinkHotspot

# --- photos

photo_3_1 = Photo(
    title="Photo 1",
    path="media/photo-1.jpg"
)

photo_nadir = Photo(
    title="Nadir photo",
    path="media/nadir.png"
)

# --- photo hotspots

photo_hotspot_3_1 = PhotoHotspot(
    photo=photo_3_1,
    pan=-15,
    tilt=17
)

# --- information hotspot

information_hotspot_2_1 = InformationHotspot(
    title="This is an information hotspot",
    pan=11,
    tilt=23
)

# --- link hotspot

link_hotspot_1_1 = LinkHotspot(
    title="This is a link hotspot",
    pan=13,
    tilt=27,
    url="http://www.johndoe.com"
)

# --- panoramas

panorama_1 = Panorama(
    directory="tiles_1",
    title="Panorama 1"
)

panorama_2 = Panorama(
    directory="tiles_2",
    title="Panorama 2",
    information_hotspots=[information_hotspot_2_1]
)

panorama_3 = Panorama(
    directory="tiles_3",
    title="Panorama 3",
    photo_hotspots=[photo_hotspot_3_1],
)

# --- panorama hotspots

panorama_hotspot_1_2 = PanoramaHotspot(panorama=panorama_2, pan=30, tilt=5, show_information=True)
panorama_hotspot_1_3 = PanoramaHotspot(panorama=panorama_3, pan=57, tilt=11, show_information=True)
panorama_hotspot_2_3 = PanoramaHotspot(panorama=panorama_3, pan=30, tilt=5, show_information=True)
panorama_hotspot_3_1 = PanoramaHotspot(panorama=panorama_1, pan=30, tilt=5, show_information=True)

panorama_1.panorama_hotspots.extend([panorama_hotspot_1_2, panorama_hotspot_1_3])
panorama_2.panorama_hotspots.append(panorama_hotspot_2_3)
panorama_3.panorama_hotspots.append(panorama_hotspot_3_1)

panorama_1.link_hotspots.append(link_hotspot_1_1)

# --- tour

tour = Tour(
    title="Tour exemple",
    first_panorama=panorama_2,
    panoramas=[panorama_1, panorama_2, panorama_3],
    nadir=photo_nadir,
)
