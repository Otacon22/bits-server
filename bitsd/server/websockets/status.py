#
# Copyright (C) 2013 Stefano Sanfilippo
# Copyright (C) 2013 BITS development team
#
# This file is part of bitsd, which is released under the terms of
# GNU GPLv3. See COPYING at top level for more information.
#

"""
Status broadcaster and handlers.
"""

import tornado.websocket

from .notifier import MessageNotifier

from bitsd.common import LOG
from .. import get_latest_data


class StatusHandler(tornado.websocket.WebSocketHandler):
    """Handler for POuL status via websocket"""

    CLIENTS = MessageNotifier('Status handler queue')

    def open(self):
        """Register new handler with MessageNotifier."""
        StatusHandler.CLIENTS.register(self)
        self.write_message(get_latest_data())

    def on_message(self, message):
        """Disconnect clients sending data (they should not)."""
        LOG.warning('Client sent a message: disconnected.')

    def on_close(self):
        """Unregister this handler when the connection is closed."""
        StatusHandler.CLIENTS.unregister(self)


def broadcast_status(message):
    """Broadcast given message to all clients. `message`
    may be either a string, which is directly broadcasted, or a dictionay
    that is JSON-serialized automagically before sending."""
    StatusHandler.CLIENTS.broadcast(message)
