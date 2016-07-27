# -*- coding: utf-8 -*-

from model import Map, Panorama, PanoramaMapping, Photo, Tour
from model import GalleryHotspot, InformationHotspot, PanoramaHotspot
from model import PhotoHotspot, LinkHotspot

# --- photos

photo_1 = Photo(
    title="Photo 1",
    path="media/photo1.jpg"
)

photo_2 = Photo(
    title="Photo 2",
    path="media/photo2.jpg"
)

photo_3 = Photo(
    title="Photo 3",
    path="media/photo3.jpg"
)

photo_4 = Photo(
    title="Panorama mapping photo",
    path="media/map_photo.png"
)

photo_5 = Photo(
    title="Nadir photo",
    path="media/nadir.png"
)

# --- photo hotspots

photo_hotspot_1 = PhotoHotspot(
    photo=photo_1,
    pan=11.1,
    tilt=22.2
)

photo_hotspot_2 = PhotoHotspot(
    photo=photo_2,
    pan=11.2,
    tilt=22.3
)

photo_hotspot_3 = PhotoHotspot(
    photo=photo_3,
    pan=12.2,
    tilt=23.3
)

# --- gallery hotspots

gallery_hotspot_1 = GalleryHotspot(
    title="Gallery 1",
    pan=23,
    tilt=57,
    photos=[photo_1, photo_2, photo_3]
)

# --- information hotspot

information_hotspot = InformationHotspot(
    title="This is an information hotspot",
    pan=11,
    tilt=23
)

# --- link hotspot

link_hotspot = LinkHotspot(
    title="This is a link hotspot",
    pan=13,
    tilt=27,
    url="http://www.johndoe.com"
)

# --- panoramas

panorama_1 = Panorama(
    directory="repertoire_1",
    title="Panorama 1",
    gallery_hotspots=[gallery_hotspot_1],
    photo_hotspots=[photo_hotspot_1]
)

panorama_2 = Panorama(
    directory="repertoire_2",
    title="Panorama 2",
    photo_hotspots=[photo_hotspot_2],
    information_hotspots=[information_hotspot]
)

panorama_3 = Panorama(
    directory="repertoire_3",
    title="Panorama 3",
    photo_hotspots=[photo_hotspot_2, photo_hotspot_3],
    link_hotspots=[link_hotspot]
)

# --- panorama hotspots

panorama_hotspot_1_2 = PanoramaHotspot(panorama=panorama_2, pan=30, tilt=5, show_information=True)
panorama_hotspot_1_3 = PanoramaHotspot(panorama=panorama_3, pan=40, tilt=10, show_information=False)
panorama_hotspot_2_1 = PanoramaHotspot(panorama=panorama_1, pan=25, tilt=3, show_information=False)
panorama_hotspot_3_2 = PanoramaHotspot(panorama=panorama_2, pan=13, tilt=9, show_information=True)

panorama_1.panorama_hotspots.extend([panorama_hotspot_1_2, panorama_hotspot_1_3])
panorama_2.panorama_hotspots.append(panorama_hotspot_2_1)
panorama_3.panorama_hotspots.append(panorama_hotspot_3_2)

# --- panorama mapping

panorama_mapping_1 = PanoramaMapping(
    panorama=panorama_1,
    x=4,
    y=6
)

panorama_mapping_2 = PanoramaMapping(
    panorama=panorama_2,
    x=7,
    y=9
)

# --- mapping

map_1 = Map(
    photo=photo_4,
    panorama_mappings=[panorama_mapping_1, panorama_mapping_2]
)

# --- tour

tour = Tour(
    title="Tour exemple",
    first_panorama=panorama_3,
    panoramas=[panorama_1, panorama_2, panorama_3],
    maps=[map_1],
    nadir=photo_5,
)
