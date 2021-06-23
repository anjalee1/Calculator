from http.server import HTTPServer, BaseHTTPRequestHandler
import cgi

result =['']
class CalHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        output = '''<html><body><h1>CALCULATOR</h1>
                    <form method= "POST" enctype="multipart/form-data" action="/" >
                    <labe>SELECT OPERATOR:</label>
                    <input type="radio" id="Addition" name="Operator" value="add">
                    <label for="Addition">Addition</label>
                    <input type="radio" id="Substraction" name="Operator" value="sub">
                   <label for="Substraction">Substraction</label>
                  <input type="radio" id="Multiplication" name="Operator" value="mul">
                  <label for="Multiplication">Multiplication</label>
                  <input  type="radio" id="Division"name="Operator" value="div">
                  <label  for="Division">Division</label> <br><br>
                  <label for="first">Enter First Number:</label><br>
                  <input type="number"  step="1" id="first"name="val1" ><br><br>
                  <label for="Second">Enter Second Number:</label><br>
                  <input type="number" step="1" id="second"name="val2"><br><br>
                  <input type="submit" value="Submit">
                  <input  type="reset">
                           </form>
                           <p>RESULT:</p></body>   </html>
                    '''
        output += f'{result[-1]}'
        self.wfile.write(output.encode())

    def do_POST(self):
            global result
            ctype,pdict=cgi.parse_header(self.headers.get('content-type'))
            pdict['boundary'] = bytes(pdict['boundary'], "utf-8")
            content_len = int(self.headers.get('Content-length'))
            pdict['CONTENT-LENGTH'] = content_len
            if ctype=='multipart/form-data':
                fields=cgi.parse_multipart(self.rfile,pdict)

                lst=list()
                op =fields.get("Operator")
                a= op[0]
                print(type(a))
                n1=fields.get("val1")
                n2=fields.get("val2")
                lst.append(a)
                lst.append(n1[0])
                lst.append(n2[0])
                print(lst)
                if lst[0]== "add":
                    val= int(lst[1])+int(lst[2])
                    a=f'{lst[1]} + {lst[2]} = {val} '

                    result.append(a)

                if lst[0]== "sub":
                    val= int(lst[1])-int(lst[2])
                    a=f'{lst[1]} - {lst[2]} = {val} '
                    result.append(a)

                if lst[0]== "mul":
                    val= int(lst[1])*int(lst[2])
                    a = f'{lst[1]} * {lst[2]} = {val} '
                    result.append(a)

                if lst[0]== "div":
                    val= int(lst[1])/int(lst[2])
                    a = f'{lst[1]} / {lst[2]} = {val} '
                    result.append(a)


            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.send_header('Location', '/')
            self.end_headers()



server = HTTPServer(('localhost',8080),CalHandler)
server.serve_forever()

