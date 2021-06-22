from http.server import HTTPServer, BaseHTTPRequestHandler

import client


# data1 = data
class CalHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/json')
        self.end_headers()

        self.wfile.write(client.data.encode())
    # def do_POST(self):
    #      for x in data1:
    #          if data1[x] =


server = HTTPServer(('localhost',8080),CalHandler)
server.serve_forever()
