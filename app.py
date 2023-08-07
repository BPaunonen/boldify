from flask import Flask, render_template, request, jsonify
import re


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/boldify", methods=["POST"])
def boldify():
    if request.json is None:
        return jsonify({"error": "No JSON payload provided"})
    text = request.json.get("text")
    if text is None:
        return jsonify({"error": "No 'text' field provided in JSON payload"})
    text = text.replace("\r\n", "\n")
    paragraphs = text.split("\\n")  # Split text into paragraphs
    bold_paragraphs = [boldify_paragraph(paragraph) for paragraph in paragraphs]
    bold_text = "\n".join(bold_paragraphs)  # Join boldified paragraphs with single newline
    return jsonify({"boldText": bold_text})



def boldify_paragraph(paragraph):
    words = paragraph.split(" ")
    bold_words = [boldify_word(word) for word in words]
    bold_paragraph = " ".join(bold_words)
    return bold_paragraph

# def boldify_paragraph(paragraph):
#     words = re.split(r'\W+', paragraph)
#     bold_words = [boldify_word(word) for word in words]
#     bold_paragraph = " ".join(bold_words)
#     return bold_paragraph

def boldify_word(word):
    if len(word) == 2:
        return f"<b>{word[0]}</b>{word[1]}"
    elif len(word) == 3:
        return f"<b>{word[:2]}</b>{word[2:]}"
    elif len(word) == 4:
        return f"<b>{word[:2]}</b>{word[2:]}"
    elif len(word) == 5:
        return f"<b>{word[:3]}</b>{word[3:]}"
    elif len(word) > 5:
        if len(word) % 2 == 0:
            bold_length = len(word) // 2
            return f"<b>{word[:bold_length]}</b>{word[bold_length:]}"
        else:
            bold_length = len(word) // 2 + 1
            return f"<b>{word[:bold_length]}</b>{word[bold_length:]}"
    else:
        return word


if __name__ == "__main__":
    app.run(debug=True)