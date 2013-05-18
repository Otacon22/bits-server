#
# Copyright (C) 2013 Stefano Sanfilippo
# Copyright (C) 2013 BITS development team
#
# This file is part of bitsd, which is released under the terms of
# GNU GPLv3. See COPYING at top level for more information.
#

"""
JSON data page handlers.
"""

import tornado.web

from .. import get_latest_data


class DataPageHandler(tornado.web.RequestHandler):
    """Get BITS data in JSON, machine parseable."""
    def get(self):
        self.write(get_latest_data())
        self.finish()
