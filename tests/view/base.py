# Case Conductor is a Test Case Management system.
# Copyright (C) 2011-2012 Mozilla
#
# This file is part of Case Conductor.
#
# Case Conductor is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Case Conductor is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Case Conductor.  If not, see <http://www.gnu.org/licenses/>.
"""
Utility base TestCase for testing views.

"""
from django_webtest import WebTest

from .. import factories as F



class ViewTestCase(WebTest):
    def setUp(self):
        """Set-up for all view test cases."""
        self.user = F.UserFactory.create()


    def add_perm(self, codename):
        """Add named permission to user."""
        from cc import model
        perm = model.Permission.objects.get(codename=codename)
        self.user.user_permissions.add(perm)
