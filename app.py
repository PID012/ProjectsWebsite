from flask import Flask, render_template_string

app = Flask(__name__)

projects = [
    {"name": "Feuer- & Raucherkennung", "status": "In Bearbeitung"},
    {"name": "Drehorgel-Touchscreen", "status": "Abgeschlossen"},
]

TEMPLATE = """
<!DOCTYPE html>
<html lang="de">
<head><meta charset="UTF-8"><title>Meine Projekte</title></head>
<body>
<h1>Projektübersicht</h1>
<table border="1">
<tr><th>Projekt</th><th>Status</th></tr>
{% for p in projects %}
<tr><td>{{ p.name }}</td><td>{{ p.status }}</td></tr>
{% endfor %}
</table>
</body></html>
"""

@app.route("/")
def home():
    return render_template_string(TEMPLATE, projects=projects)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
