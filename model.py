# -*- coding: utf-8 -*-


class Tour:
    id = 0

    def __init__(self, **kwargs):
        Tour.id += 1
        self.id = Tour.id

        self.title = kwargs.get("title")
        self.dropmenu = kwargs.get("dropmenu", False)
        self.viewfinder = kwargs.get("viewfinder", False)
        self.scrollmenu = kwargs.get("scrollmenu", False)
        self.zoomslider = kwargs.get("zoomslider", False)
        self.auto_rotation = kwargs.get("auto_rotation", False)
        self.full_screener = kwargs.get("full_screener", False)
        self.compass = kwargs.get("compass", False)

        self.facebook_metadata = kwargs.get("facebook_metadata")

        self.first_panorama = kwargs.get("first_panorama")
        # self.photo_size = models.ForeignKey(PhotoSize, blank=True, null=True)
        self.nadir = kwargs.get("nadir")

        self.panoramas = kwargs.get("panoramas", [])
        self.maps = kwargs.get("maps", [])


class Panorama:
    id = 0

    def __init__(self, **kwargs):
        Panorama.id += 1
        self.id = Panorama.id

        self.title = kwargs.get("title")
        self.directory = kwargs.get("directory", "")
        self.initial_pan = kwargs.get("initial_pan")
        self.initial_tilt = kwargs.get("initial_tilt")
        self.min_tilt = kwargs.get("min_tilt")
        self.max_tilt = kwargs.get("max_tilt")
        self.direction = kwargs.get("direction")

        self.gallery_hotspots = kwargs.get("gallery_hotspots", [])
        self.information_hotspots = kwargs.get("information_hotspots", [])
        self.link_hotspots = kwargs.get("link_hotspots", [])
        self.panorama_hotspots = []
        self.photo_hotspots = kwargs.get("photo_hotspots", [])


class PanoramaHotspot:
    def __init__(self, **kwargs):
        self.panorama = kwargs.get("panorama")
        self.show_information = kwargs.get("show_information", False)
        self.pan = kwargs.get("pan")
        self.tilt = kwargs.get("tilt")


class GalleryHotspot:
    id = 0

    def __init__(self, **kwargs):
        GalleryHotspot.id += 1
        self.id = GalleryHotspot.id

        self.title = kwargs.get("title")
        self.pan = kwargs.get("pan")
        self.tilt = kwargs.get("tilt")
        self.photos = kwargs.get("photos", [])


class Photo:
    id = 0

    def __init__(self, **kwargs):
        Photo.id += 1
        self.id = Photo.id

        self.title = kwargs.get("title")
        self.path = kwargs.get("path")


class InformationHotspot:
    id = 0

    def __init__(self, **kwargs):
        InformationHotspot.id += 1
        self.id = InformationHotspot.id

        self.title = kwargs.get("title")
        self.pan = kwargs.get("pan")
        self.tilt = kwargs.get("tilt")


class LinkHotspot:
    id = 0

    def __init__(self, **kwargs):
        LinkHotspot.id += 1
        self.id = LinkHotspot.id

        self.title = kwargs.get("title")
        self.pan = kwargs.get("pan")
        self.tilt = kwargs.get("tilt")
        self.url = kwargs.get("url")


class Map:
    id = 0

    def __init__(self, **kwargs):
        Map.id += 1
        self.id = Map.id

        self.photo = kwargs.get("photo")
        self.pan_shift = kwargs.get("pan_shift")
        self.panorama_mappings = kwargs.get("panorama_mappings", [])


class PanoramaMapping:
    def __init__(self, **kwargs):
        self.panorama = kwargs.get("panorama")
        self.x = kwargs.get("x")
        self.y = kwargs.get("y")


class FacebookMetadata:
    def __init__(self, **kwargs):
        self.description = kwargs.get("description")
        # thumb photo
        self.photo = kwargs.get("photo")
        self.height = kwargs.get("height")
        self.width = kwargs.get("width")
