from datetime import datetime
from flask import Flask

app = Flask(__name__)

# Your code here
# @app.cli.command('test')
@app.route('/current_time/')
def current_time():
    time_now = datetime.now()
    # print(time_now)
    current_time_str = time_now.strftime("%H:%M")
    print(current_time_str)
    return f'<p>{current_time_str}</p>'

if __name__ == '__main__':
    app.run(debug=True)
