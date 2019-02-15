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

def clear_viewport():
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()

def test_api_wrapper(context):
    # Create a cube as the selected, active object
    bpy.ops.mesh.primitive_cube_add(size=2, view_align=False, enter_editmode=False, location=(2, 2, 2))

    # Validate that the active object (the cube) is where we expect it to be
    active_obj = context.scene.object_api_wrapper.get_active_object()
    assert(active_obj.get_location_x() - 2.0 < 0.01)

def test_move_operator(context):
    # Create a cube as the selected, active object
    bpy.ops.mesh.primitive_cube_add(size=2, view_align=False, enter_editmode=False, location=(2, 2, 2))

    # Test the overall flow
    move_active_object(bpy.context.scene.object_api_wrapper, 1.0, 1.0, 1.0)
    for o in bpy.context.scene.objects:
        assert(o.location.x - 1.0 < 0.01)

class OBJECT_OT_MoveObjectTests(bpy.types.Operator):
    bl_idname = "object.another_move_object_test"
    bl_label = "Test the Move Object Addon!"
    bl_options = {'REGISTER'}

    def execute(self, context):
        # Clear the viewport to remove excess objects
        clear_viewport()

        # Unit test api wrapper
        test_api_wrapper(context)

        # Clear the viewport inbetween tests
        clear_viewport()

        # Test the overall flow
        test_move_operator(context)

        # Display a message in the UI letting the user know that tests have passed
        self.report({'INFO'}, "Tests Passed")

        # Let's blender know the operator is finished
        return {'FINISHED'}
