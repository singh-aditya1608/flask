import psutil
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    cpu_percent = psutil.cpu_percent()
    memory_percent = psutil.virtual_memory().percent
    Message = None
    if cpu_percent > 80 or memory_percent > 80:
        Message = "High CPU or Memory Detected, scale up!!!"
    return render_template("index.html", cpu_percent=cpu_percent, memory_percent=memory_percent, message=Message)
if __name__ == '__main__':
    app.run(debug=True, port=8001)

###
## return f'CPU usage: {cpu_percent}%'
# 
# @app.route('/memory')
 #def memory():
  #  memory_percent = psutil.virtual_memory().percent 
   # return f'memory_utilisation: {memory_percent}%'
   # return render_template('index.html', memory_percent= memory_percent)
# 
# 
# 
# 
# 
# 
#  ###
