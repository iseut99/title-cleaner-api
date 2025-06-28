from flask import Flask, request, jsonify
import re
import unicodedata

app = Flask(__name__)

def clean_title(title):
    title = unicodedata.normalize('NFKD', title).encode('ASCII', 'ignore').decode('utf-8')
    title = re.sub(r'[^\w\s\-:]', '', title)
    title = re.sub(r'\s+', ' ', title).strip()
    title = re.sub(r'\bAi\b', 'AI', title)
    return title

@app.route('/clean', methods=['POST'])
def clean():
    data = request.get_json()
    title = data.get('title', '')
    cleaned = clean_title(title)
    return jsonify({'cleaned_title': cleaned})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
