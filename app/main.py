from flask import Flask, jsonify, render_template, send_from_directory
import os

app = Flask(__name__, template_folder="templates", static_folder="static")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/health")
def health():
    return jsonify({"status": "ok"}), 200


@app.route("/api/video-metadata")
def video_metadata():
    return jsonify({"name": "sample.mp4", "duration": 10}), 200


@app.route("/static/<path:filename>")
def static_files(filename):
    return send_from_directory(app.static_folder, filename)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port, debug=True)
