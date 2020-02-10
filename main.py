from flask import Flask, render_template, redirect, request


app = Flask(__name__)


requests_get = 0
requests_post = 0
requests_put = 0
requests_delete = 0


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/request-counter', methods=['GET', 'POST', 'PUT', 'DELETE'])
def request_counter():
    if request.method == 'GET':
        global requests_get
        requests_get += 1
    elif request.method == 'POST':
        global requests_post
        requests_post += 1
    elif request.method == 'PUT':
        global requests_put
        requests_put += 1
    elif request.method == 'DELETE':
        global requests_delete
        requests_delete += 1
    with open('request_counts.txt', 'w') as my_file:
        my_file.write(f'GET: {requests_get}\nPOST: {requests_post}\nPUT: {requests_put}\nDELETE: {requests_delete}')
    return redirect('/')


@app.route('/statistics')
def statistics():
    return render_template('statistics.html', gets=requests_get, posts=requests_post, puts=requests_put,
                           deletes=requests_delete)


if __name__ == '__main__':
    app.run(debug=True)
