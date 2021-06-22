from http.server import HTTPServer, BaseHTTPRequestHandler
import json

# data1 = data
class CalHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        # operator = input('''Type one of the opertaors from these options:
        #                  + : For addition
        #                  - : For substraction
        #                  * : For multiplication
        #                  / : For Divison
        #
        #                  Type here: ''')
        #
        # num1 = int(input('Enter First Number:'))
        # num2 = int(input('Enter Second Number:'))
        # data = {'operator': '', 'num1': '', 'num2': ''}
        # data['operator'] = operator
        # data['num1'] = num1
        # data['num2'] = num2
        output = '''<html><body><h1>CALCULATOR</h1>
                    <form>
                    <labe>SELECT OPERATOR:</label>
                    <input type="radio" id="Addition" name="Operator" value="add">
                    <label for="Addition">Addition</label>
                    <input type="radio" id="Substraction" name="Operator" value="sub">
                   <label for="Substraction">Substraction</label>
                  <input type="radio" id="Multiplication" name="Operator" value="Multiplication">
                  <label for="Multiplication">Multiplication</label>
                  <input  type="radio" id="Division"name="Operator" value="Division">
                  <label  for="Division">Division</label> <br><br>
                  <label for="first">Enter First Number:</label><br>
                  <input type="text" id="first"name="val1" ><br><br>
                  <label for="Second">Enter Second Number:</label><br>
                  <input type="text" id="second"name="val2"><br><br>
                  <input type="submit" value="Submit">
                  <input  type="reset">
                           </form> </body>   </html>   
                    '''

        self.wfile.write(output.encode())



server = HTTPServer(('localhost',8080),CalHandler)
server.serve_forever()
