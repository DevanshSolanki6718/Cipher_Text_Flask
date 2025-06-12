from flask import Flask, render_template, request
import webbrowser
import threading

app = Flask(__name__)

def shift_char_encrypt(char, key):
    if 'A' <= char <= 'Z':
        return chr((ord(char) - ord('A') + key) % 26 + ord('A'))
    elif 'a' <= char <= 'z':
        return chr((ord(char) - ord('a') + key) % 26 + ord('a'))
    else:
        temp = ord(char) + key
        if 65 <= temp <= 90 or 97 <= temp <= 122:
            temp += 26
        return chr(temp)

def shift_char_decrypt(char, key):
    if 'A' <= char <= 'Z':
        return chr((ord(char) - ord('A') - key) % 26 + ord('A'))
    elif 'a' <= char <= 'z':
        return chr((ord(char) - ord('a') - key) % 26 + ord('a'))
    else:
        temp = ord(char) - key
        if 65 <= temp <= 90 or 97 <= temp <= 122:
            temp -= 26
        return chr(temp)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ''
    if request.method == 'POST':
        message = request.form['message']
        key = int(request.form['key']) % 26
        action = request.form['action']
        if action == 'encrypt':
            result = ''.join(shift_char_encrypt(c, key) for c in message)
        else:
            result = ''.join(shift_char_decrypt(c, key) for c in message)
    return render_template('index.html', result=result)

def open_browser():
    webbrowser.open_new('http://127.0.0.1:5000')

if __name__ == '__main__':
    from threading import Timer
    import webbrowser

    def open_browser():
        webbrowser.open_new('http://127.0.0.1:5000')

    # Only run browser once when reloader is not active
    Timer(1, open_browser).start()
    app.run(debug=True, use_reloader=False)