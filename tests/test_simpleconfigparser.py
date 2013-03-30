import sys
import os
from os.path import join, realpath, dirname, exists

try:
    from simpleconfigparser import simpleconfigparser
except ImportError:
    print('Unable to import simpleconfigparser.  Is it installed?')
    sys.exit(1)

try:
    import py.test
except ImportError:
    print('Unable to import py.test.  Is py.test installed?')
    sys.exit(1)

# figure out the base path to use for file include
test_path = realpath(dirname(__file__))


class TestSimpleconfigparser:
    def test_read_quote_stripping(self):
        config = simpleconfigparser()
        config.read(join(test_path, 'quotes.ini'))
        assert config.section.single == 'win'
        assert config.section.double == 'win again'
        assert config['section']['single'] == 'win'
        assert config['section']['double'] == 'win again'

    def test_read_without_quotes(self):
        config = simpleconfigparser()
        config.read(join(test_path, 'without-quotes.ini'))
        assert config.section.item == 'not-default'
        assert config['section']['item'] == 'not-default'

    def test_read_section_missing(self):
        config = simpleconfigparser()
        assert config.fake.it is None
        assert config['fake']['it'] is None

    def test_read_item_missing(self):
        config = simpleconfigparser()
        config.fake.me = 'boo'
        assert config.fake.it is None
        assert config['fake']['it'] is None

    def test_defaults(self):
        defaults = {
            'section': {
                'item': 'default'
            }
        }

        config = simpleconfigparser(defaults=defaults)
        assert config.section.item == 'default'
        assert config['section']['item'] == 'default'

    def test_defaults_read_ini(self):
        defaults = {
            'section': {
                'item': 'default'
            }
        }

        config = simpleconfigparser(defaults=defaults)
        config.read(join(test_path, 'not-default.ini'))
        assert config.section.item == 'not-default'
        assert config['section']['item'] == 'not-default'

    def test_read_types(self):
        config = simpleconfigparser()
        config.read(join(test_path, 'types.ini'))
        assert int(config.types.int) == 6
        assert int(config.types.int2) == 7
        assert float(config.types.float) == 6.5
        assert float(config.types.float2) == 8.5
        assert config.types.getboolean('boolean_yes_1') is True
        assert config.types.getboolean('boolean_yes_2') is True
        assert config.types.getboolean('boolean_yes_3') is True
        assert config.types.getboolean('boolean_no_1') is False
        assert config.types.getboolean('boolean_no_2') is False
        assert config.types.getboolean('boolean_no_3') is False

    def test_read_types_dict_format(self):
        config = simpleconfigparser()
        config.read(join(test_path, 'types.ini'))
        assert int(config['types']['int']) == 6
        assert int(config['types']['int2']) == 7
        assert float(config['types']['float']) == 6.5
        assert float(config['types']['float2']) == 8.5
        assert config['types'].getboolean('boolean_yes_1') is True
        assert config['types'].getboolean('boolean_yes_2') is True
        assert config['types'].getboolean('boolean_yes_3') is True
        assert config['types'].getboolean('boolean_no_1') is False
        assert config['types'].getboolean('boolean_no_2') is False
        assert config['types'].getboolean('boolean_no_3') is False

    def test_read_items(self):
        config = simpleconfigparser()
        config.read(join(test_path, 'quotes.ini'))
        items = [
            ('single', "win"),
            ('double', "win again")
        ]

        assert config.section.items() == items

    def test_write(self, tmpdir):
        path = join(str(tmpdir), 'new.ini')
        text = b"""[add]
this = woo!

"""

        config = simpleconfigparser()
        config.add.this = 'woo!'
        with open(path, 'w') as handle:
            config.write(handle)

        assert exists(path) is True
        with open(path, 'rb') as handle:
            content = handle.read()
            assert text == content
        os.remove(path)
