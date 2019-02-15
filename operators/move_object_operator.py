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

from ..addon_logic.move_object import move_active_object

class OBJECT_OT_MoveObject(bpy.types.Operator):
    bl_idname = "object.another_move_object"
    bl_label = "Move Active Object"
    bl_options = {'REGISTER'}
    # Properties use ':' instead of '='
    # per change notes for Blender2.80 release
    # https://wiki.blender.org/wiki/Reference/Release_Notes/2.80/Python_API/Addons
    x: bpy.props.FloatProperty(name="X", default=0.0)
    y: bpy.props.FloatProperty(name="Y", default=0.0)
    z: bpy.props.FloatProperty(name="Z", default=0.0)

    def execute(self, context):
        move_active_object(context.scene.object_api_wrapper, self.x, self.y, self.z)

        # Let's blender know the operator is finished
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)
