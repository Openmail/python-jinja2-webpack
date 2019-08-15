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
    foo = {
        'errors': [],
        'warnings': [],
        'publicPath': 'https://cdn.now.howstuffworks.localhost:8080/content-site/assets/quiz/',
        'entrypoints': {
            'autoversed': {
                'chunks': [
                    'autoversed'
                ],
                'assets': [
                    'autoversed.fa5bb195.js'
                ],
                'children': {},
                'childAssets': {}
            },
            'goliath': {
                'chunks': [
                    'goliath'
                ],
                'assets': [
                    'goliath.bab312ea.js',
                    'goliathMoreStuff.bab312ea.js'
                ],
                'children': {},
                'childAssets': {}
            }
        }
    }

    env = Environment(stats=foo, manifest=None)
    f = WebpackFilter(env)
    assert f
    assert f('autoversed') == 'https://cdn.now.howstuffworks.localhost:8080/content-site/assets/quiz/autoversed.fa5bb195.js'
