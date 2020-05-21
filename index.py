import os
import sys
from abc import ABC

import tornado.ioloop
import tornado.web


class BasicRequestHandler(tornado.web.RequestHandler, ABC):
    def get(self):
        self.write(f"Served from {os.getpid()}")


if __name__ == "__main__":
    app = tornado.web.Application([(r"/", BasicRequestHandler)])

    port = 8888
    if sys.argv.__len__() > 1:
        port = sys.argv[1]

    app.listen(port)
    print(f"Application is ready and listening on port {port}.")
    tornado.ioloop.IOLoop.current().start()
