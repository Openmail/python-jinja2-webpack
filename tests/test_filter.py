import pytest

from jinja2_webpack import AssetNotFoundException, Environment
from jinja2_webpack.filter import WebpackFilter


def test_filter_defined():
    assert WebpackFilter


def test_simple_lookup():
    env = Environment(manifest={'a': 'b'})
    f = WebpackFilter(env)
    assert f
    assert f('a') == '/static/pack/b'


def test_basename_lookup():
    env = Environment(manifest={'a': 'b'})
    f = WebpackFilter(env)
    assert f('/path/to/a') == '/static/pack/b'


def test_invalid_empty():
    env = Environment(manifest=None, errorOnInvalidReference=False)
    f = WebpackFilter(env)
    assert f('a') is None


def test_invalid_error():
    env = Environment(manifest=None, errorOnInvalidReference=True)
    f = WebpackFilter(env)
    with pytest.raises(AssetNotFoundException):
        f('a')


def test_stats_lookup():
    stats = {
        'publicPath': 'https://cdn.foo.com/',
        'entrypoints': {
            'a': {
                'chunks': [
                    'a-chunk'
                ],
                'assets': [
                    'a-asset-1.js'
                ],
                'children': {},
                'childAssets': {}
            },
            'b': {
                'chunks': [
                    'b-chunk'
                ],
                'assets': [
                    'b-asset-1.js',
                    'b-asset-2.js'
                ],
                'children': {},
                'childAssets': {}
            }
        }
    }

    env = Environment(stats=stats, manifest=None)
    f = WebpackFilter(env)
    assert f
    assert f('a') == 'https://cdn.foo.com/a-asset-1.js'
    assert f('b') == (
        'https://cdn.foo.com/b-asset-1.js\nhttps://cdn.foo.com/b-asset-2.js'
    )
