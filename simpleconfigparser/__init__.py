# -*- coding: utf-8 -*-
"""
The MIT License

Copyright (c) 2013 Helgi Þorbjörnsson <helgi@php.net>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

try:
    from configparser import configparser, NoOptionError, NoSectionError
except ImportError:
    from ConfigParser import SafeConfigParser as configparser, NoOptionError, NoSectionError
import collections


class simpleconfigparser(configparser):
    class Section(object):
        """
        Contain the section specific items that can be accessed via object properties
        """
        parser = None
        section = None

        def __init__(self, section, parser):
            self.section = section
            self.parser = parser

        def __getattr__(self, name, raw=False, vars=None):
            if name not in simpleconfigparser.Section.__dict__:
                return self.parser.get(self.section, name, raw, vars)

        def __setattr__(self, name, value):
            if name in simpleconfigparser.Section.__dict__:
                return object.__setattr__(self, name, value)

            return self.parser.set(self.section, name, value)

        def getboolean(self, name):
            if not self.section:
                return None

            return self.parser.getboolean(self.section, name)

        def items(self):
            if not self.section:
                return None

            items = []
            for key, value in self.parser.items(self.section):
                # strip quotes
                items.append((key, value.strip('"\'')))

            return items

    def __init__(self, defaults=None, dict_type=collections.OrderedDict, allow_no_value=False):
        configparser.__init__(self, defaults, dict_type, allow_no_value)
        # Improved defaults handling
        if isinstance(defaults, dict):
            for section, values in defaults.iteritems():
                if section not in self.sections():
                    self.add_section(section)

                for name, value in values.iteritems():
                    self.set(section, name, str(value))

    def __getattr__(self, name, raw=False, vars=None):
        if name not in simpleconfigparser.__dict__:
            if name not in self.sections():
                self.add_section(name)

            return simpleconfigparser.Section(name, self)

        return None

    def set(self, section, option, value=None):
        try:
            return configparser.set(self, section, option, value)
        except NoSectionError:
            return None

    def get(self, section, option, raw=False, vars=None):
        try:
            # Strip out quotes from the edges
            return configparser.get(self, section, option, raw, vars).strip('"\'')
        except NoOptionError:
            return None
