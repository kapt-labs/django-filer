from image_cropping.backends.easy_thumbs import EasyThumbnailsBackend
from image_cropping.widgets import ImageCropWidget


class FilerBackend(EasyThumbnailsBackend):
    WIDGETS = dict(EasyThumbnailsBackend.WIDGETS)
    WIDGETS['MultiStorageFileField'] = ImageCropWidget
