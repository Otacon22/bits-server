#import tornado.tcpserver TODO Tornado 3.0
import tornado.netutil

from tornado.options import options

from bitsd.common import LOG

class RemoteServer(tornado.netutil.TCPServer):
    """Handle incoming commands via BITS mini protocol."""

    # TODO
    ACTIONS = {
        'temperature': lambda sensorno, value: pass,
        'status': lambda status: pass,
        'enter': lambda id: pass,
        'leave': lambda id: pass,
    }

    def handle_stream(self, stream, address):
        """Handles inbound TCP connections asynchronously."""
        if address[0] != options.fonera_address:
            LOG.error("Receiving commands from {}, expected from '{}'. Ignoring.".format(
            address, options.fonera_address))
            return
        stream.read_until_close(self.handle_commands)

    def handle_commands(self, message):
        """Reacts to received commands (callback).
        Will split single commands, separate args and call appropriate handlers."""
        for command in message.split(b'\n'):
            if command:
                LOG.info('Received command `{}` from Fonera, executing.'.format(command))
                args = command.split(b' ')
                # Execute handler (index 0) with args (index 1->end)
                ACTIONS[args[0]](*args[1:])
