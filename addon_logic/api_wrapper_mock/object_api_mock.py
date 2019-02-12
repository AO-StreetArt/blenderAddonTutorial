'''
Copyright (C) 2019 Alex Barry
aostreetart9@gmail.com

Created by Alex Barry

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

from unittest.mock import MagicMock

class Object3dMock(object):
    def __init__(self, location):
        self.location = location

    def get_location_x(self):
        return self.location[0]

    def set_location_x(self, new_loc):
        self.location[0] = new_loc

    def get_location_y(self):
        return self.location[1]

    def set_location_y(self, new_loc):
        self.location[1] = new_loc

    def get_location_z(self):
        return self.location[2]

    def set_location_z(self, new_loc):
        self.location[2] = new_loc

class ObjectApiMock(object):
    get_active_object = MagicMock()
