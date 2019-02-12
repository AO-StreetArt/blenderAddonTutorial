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

import bpy

class Object3dWrapper(object):
    def __init__(self, blender_object):
        self.blender_obj_ref = blender_object

    def get_location_x(self):
        return self.blender_obj_ref.location.x

    def set_location_x(self, new_loc):
        self.blender_obj_ref.location.x = new_loc

    def get_location_y(self):
        return self.blender_obj_ref.location.y

    def set_location_y(self, new_loc):
        self.blender_obj_ref.location.y = new_loc

    def get_location_z(self):
        return self.blender_obj_ref.location.z

    def set_location_z(self, new_loc):
        self.blender_obj_ref.location.z = new_loc

class ObjectApiWrapper(object):
    # Get the active object within a Blender context
    def get_active_object(self):
        active_obj = None
        for o in bpy.context.scene.objects:
            if o.select_get():
                return Object3dWrapper(o)
