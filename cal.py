from http.server import HTTPServer, BaseHTTPRequestHandler


# data1 = data
class CalHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/json')
        self.end_headers()
        operator = input('''Type one of the opertaors from these options:
                         + : For addition
                         - : For substraction
                         * : For multiplication
                         / : For Divison

                         Type here: ''')

        num1 = int(input('Enter First Number:'))
        num2 = int(input('Enter Second Number:'))
        data = {'operator': '', 'num1': '', 'num2': ''}
        data['operator'] = operator
        data['num1'] = num1
        data['num2'] = num2
        self.wfile.write(data.encode())



server = HTTPServer(('localhost',8080),CalHandler)
server.serve_forever()
