app/routes.py: Return complete HTML page from view function

from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Jud'}
    return '''
<html>
    <head>
        <title>Home Page - Microblog</title>
    </head>
    <body>
        <h1>Hello from Mars, ''' + user['username'] + '''!</h1>
    </body>
</html>'''
