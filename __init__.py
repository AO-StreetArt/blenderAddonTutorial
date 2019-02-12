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

bl_info = {
    "name": "moveObjectAddon",
    "description": "Demo Blender Add-on to show Layered Architecture",
    "author": "Alex Barry",
    "version": (0, 0, 3),
    "blender": (2, 80, 0),
    "location": "View3D",
    "warning": "This addon is still in development.",
    "wiki_url": "",
    "category": "Object" }

import traceback

# Load or reload submodules
# This handles what happens when we first enable addon vs when we
# switch it off then on again

if "bpy" in locals():
    import importlib
    importlib.reload(object_api_wrapper)
    importlib.reload(move_object_operator)
else:
    from .api_wrapper import object_api_wrapper
    from .operators import move_object_operator, test_operators

import bpy

# Registration for each class individually,
# per change notes for Blender2.8 release
# https://wiki.blender.org/wiki/Reference/Release_Notes/2.80/Python_API/Addons
classes = [move_object_operator.OBJECT_OT_MoveObject, test_operators.OBJECT_OT_MoveObjectTests]

def register():
    # Register modules
    try:
        for cls in classes:
            bpy.utils.register_class(cls)
    except:
        traceback.print_exc()

    # Store the API Wrapper as a Scene attribute
    bpy.types.Scene.object_api_wrapper = object_api_wrapper.ObjectApiWrapper()

def unregister():
    # Cleanup the data we stored in the scene
    del bpy.types.Scene.object_api_wrapper

    # Unregister modules
    try:
        for cls in reversed(classes):
            bpy.utils.unregister_class(cls)
    except:
        traceback.print_exc()

    print("Unregistered {}".format(bl_info["name"]))
