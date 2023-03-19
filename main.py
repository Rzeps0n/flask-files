from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def file_list():
    file_list = os.listdir('.')
    file_info = []
    for file_name in file_list:
        file_type = 'directory' if os.path.isdir(file_name) else os.path.splitext(file_name)[1]
        file_info.append((file_name, file_type))
    return """
    <h1>Files:</h1>
    <ul>
    %s
    </ul>
    """ % ''.join(['<li>%s - (%s)</li>' % (name, type) for name, type in file_info])

if __name__ == '__main__':
    app.run(host='0.0.0.0')