# -*- coding: utf-8 -*-

import time, BaseHTTPServer, os
import cgi
from article import *

import urlparse, traceback, subprocess

HOST_NAME = 'localhost'
PORT_NUMBER = 7777

class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_HEAD(s):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
    def do_POST(s):
        return s.do_GET()
    def do_GET(s):
        """Respond to a GET request."""
        timer = time.time()
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()

        try:
            ctype, pdict = cgi.parse_header(s.headers.getheader('content-type'))
            if ctype == 'multipart/form-data':
                post = cgi.parse_multipart(s.rfile, pdict)
            elif ctype == 'application/x-www-form-urlencoded':
                length = int(s.headers.getheader('content-length'))
                post = cgi.parse_qs(s.rfile.read(length), keep_blank_values=1)
            else:
                post = {}
        except:
            post = {}

        o = urlparse.urlparse(s.path)
        get = urlparse.parse_qs(o.query)

        if '/favicon.ico' == o.path:
            return

        text1 = post['text1'][0] if 'text1' in post else article1DefaultText
        text2 = post['text2'][0] if 'text2' in post else article2DefaultText
        try:
            Article.shingleLength = int(post['shingleLength'][0])
        except:
            Article.shingleLength = defaultShingleLength
        text1 = text1.decode('utf-8')
        text2 = text2.decode('utf-8')

        article1 = Article(text1)
        article2 = Article(text2)
        ShinglesComparer.compare(article1, article2)
        htmlShingles1 = article1.getColoredText('<span style="background-color: yellow;">', '</span>').replace('\n', '<br>')
        htmlShingles2 = article2.getColoredText('<span style="background-color: yellow;">', '</span>').replace('\n', '<br>')

        article1 = Article(text1)
        article2 = Article(text2)
        IMatchComparer.compare(article1, article2)
        htmlIMatch1 = article1.getColoredText('<span style="background-color: yellow;">', '</span>').replace('\n', '<br>')
        htmlIMatch2 = article2.getColoredText('<span style="background-color: yellow;">', '</span>').replace('\n', '<br>')

        out = u"""
<html>
	<head>
	    <meta http-equiv="content-type" content="text/html;charset=utf-8">"""
        out += u'<style>' + fileGet('style/style.css').decode('utf8') + u"""</style>
		<title> Антиплагиат для русского языка </title>
	</head>
	<body>
		<form method="post" action="http://""" + HOST_NAME + u':' + str(PORT_NUMBER) + u"""">
			<input class="compare" type="submit" value="Сравнить">
			<label for="shingleLength">Длина шингла</label>
			<select name="shingleLength" class="select">"""
        for i in range(3, 9):
            out += u'<option' + (u' selected="selected"' if i == Article.shingleLength else u'') + u'>' + str(i) + u'</option>'
        out += u"""
            </select>
			<table width="96%">
			    <tr>
					<td>
						<textarea name="text1" cols="90" rows="10">""" + text1 + u"""</textarea>
					</td>
					<td>
						<textarea name="text2" cols="90" rows="10">""" + text2 + u"""</textarea>
					</td>
				</tr>
				<tr><td><h1>Результаты метода шинглов</h1><td></tr>
				<tr>
					<td>
						<div style="background-color: ghostwhite;">""" + htmlShingles1 + u"""</div>
					</td>
					<td>
						<div style="background-color: ghostwhite;">""" + htmlShingles2 + u"""</div>
					</td>
				</tr>
				<tr><td><h1>Результаты метода I-Match</h1><td></tr>
				<tr>
					<td>
						<div style="background-color: ghostwhite;">""" + htmlIMatch1 + u"""</div>
					</td>
					<td>
						<div style="background-color: ghostwhite;">""" + htmlIMatch2 + u"""</div>
					</td>
				</tr>
			</table>
		</form>
	</body>
</html>"""
        s.wfile.write(out.encode('utf-8'))

if __name__ == '__main__':
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
    print time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER)
    subprocess.call('start http://%s:%d' % (HOST_NAME, PORT_NUMBER), shell=True)  # открыть вкладку в браузере
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER)