from flask import Flask,render_template
import socket
#from flask_restful import Resource, Api

import platform
import multiprocessing
#from flask_restful import Resource, Api
app = Flask(__name__)

@app.route("/")
def fetchdetails():
    hostname=socket.gethostname()
    hostip=socket.gethostbyname_ex(hostname)
    return str(hostname),str(hostip)

def ping_server():
    os_info=platform.platform()
    arch=platform.architecture()
    num_cpus=multiprocessing.cpu_count()
    
    return f' Welcome latest release: {os_info}<br>No of CPUs: {num_cpus}<br>Architecture: {arch}'

@app.route("/details")
def detail():
    hostname,ip=fetchdetails()
    return render_template('index.html',HOSTNAME=hostname,IP=ip)

if __name__ == '__main__':
	app.run(debug=True, port=5003,host="0.0.0.0")