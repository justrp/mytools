#!/user/bin/env python3 -tt
# -*- coding: utf-8 -*-

import colored

class Printer(object):
    """
    Printer interface

    On creation counts how many colors will it use
    """
    
    def __init__(self, unique_strings):
        color = 1
        self.colors = {}
        self.info = {}
        for i in unique_strings:
            self.colors[i] = color
            color += 1

    def add(self, title, text):
        title_as_id = self._get_title(title)
        self.info[title_as_id] = self.info.get(title_as_id,'') + text


    def print(self):
        for title, values in self.info.items():
            print(title)
            print(values)
            print('\n')


    def _get_title(self, title):
        if type(title) is list:
            return self._multiply_title(title)
        return (colored.stylize('@' + title, colored.bg(self.colors[title])))


    def _multiply_title(self, titles):
        result = ''
        for title in titles:
            result += colored.stylize('@' + title, colored.bg(self.colors[title]))
        return result

