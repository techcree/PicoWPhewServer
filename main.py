from phew import logging, server, connect_to_wifi
from phew.template import render_template
from secret import ssid, password
from temperatur import temperatur
import access


connect_to_wifi(ssid, password)
print("open IP Adress for Website")

@server.route("/")
def index(request):
    return render_template("/index.html", name="Home", title="Home")

@server.route("/about")
def about(request):
    return render_template("/about.html", name="by TechCree I ssk", title="TechCree")

@server.route("/smart")
def about(request):
    return render_template("/smart.html", name="SmartHome", title="SmartHome")

@server.route("/login", ["POST",'GET'])
def login_form(request):
    print(request.method)
    if request.method == 'GET':
        return render_template("/login.html")
    if request.method == 'POST':    
        username = request.form.get("username", None)
        password = request.form.get("password", None)

        if username == "admin" and password == "Passwort":
            return render_template('/default.html', content = f"<h1>Hallo, {username}</h1>")
        else:
            return render_template('/default.html', content = "Invalid username or password")

@server.catchall()
def my_catchall(request):
  return "Seite nicht gefunden", 404

server.run()
