# -*- coding: utf-8 -*-

"""
Apache2 License Notice
Copyright 2018 Alex Barry
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import unittest

from move_object import move_active_object
from api_wrapper_mock.object_api_mock import ObjectApiMock, Object3dMock

class TestMoveActiveObject(unittest.TestCase):
    def test_move_object(self):
        object_api_wrapper = ObjectApiMock()
        active_object = Object3dMock([1.0, 2.0, 3.0])
        object_api_wrapper.get_active_object.return_value = active_object
        move_active_object(object_api_wrapper, 1.0, 1.0, 1.0)
        assert(active_object.get_location_x() - 2.0 < 0.01)
        assert(active_object.get_location_y() - 3.0 < 0.01)
        assert(active_object.get_location_z() - 4.0 < 0.01)
        object_api_wrapper.get_active_object.assert_called()

if __name__ == '__main__':
    unittest.main()
