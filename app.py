from . import create_app

app = create_app('default')
app_context = app.app_context()
app_context.push()

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
