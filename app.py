# app.py
# check localhost:port/api/ui

from flask import render_template
import config     # first import runs the initialisation code
from models import Person

# **********************************************
app = config.connex_app
app.add_api(config.basedir / "swagger.yml")

# **********************************************
@app.route("/")
def home():
    allpeople = Person.query.all()
    return render_template("home.html", people=allpeople)

# **********************************************
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
