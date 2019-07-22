def script(asset):
    return '<script nomodule src="%s"></script>' % asset.url

def script_module(asset):
    return '<script type="module" src="%s"></script>' % asset.url


def image(asset):
    return '<img src="%s">' % asset.url


def stylesheet(asset):
    print('--- stylesheet asset.url: ' + asset.url)
    return '<link rel="stylesheet" href="%s">' % asset.url


def url(asset):
    return asset.url
