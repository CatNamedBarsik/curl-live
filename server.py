from flask import Flask, Response
import time

app = Flask(__name__)

@app.route('/')
def artifact():
    def stream():
        frames = [
            "╭━━━╮╱╱╱╱╱╱╱╱╱╱",
            "┃╭━╮┃╱╱╱╱╱╱╱╱╱╱",
            "┃╰━╯┣━━┳━╮╭━━╮",
            "┃╭╮╭┫╭╮┃╭╮┫━━┫",
            "┃┃┃╰┫╭╮┃┃┃┣━━┃",
            "╰╯╰━┻╯╰┻╯╰┻━━╯"
        ]
        for frame in frames:
            yield frame + '\n'
            time.sleep(0.3)
    return Response(stream(), mimetype='text/plain')

app.run(host='0.0.0.0', port=10000)
