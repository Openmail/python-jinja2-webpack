class WebpackFilter(object):
    """ Jinja2 filter which can be used to reference webpack assets from
    jinja2 templates """
    def __init__(self, environment):
        self.environment = environment

    def __call__(self, assetspec):
        assets = self.environment.identify_assetspec(assetspec)
        if assets:
            return self.environment.render_assets(assets)
