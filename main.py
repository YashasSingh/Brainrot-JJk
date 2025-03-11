from flask import Flask, jsonify, request, send_file
import random
import os

app = Flask(__name__)

# Sample JJK quotes
quotes = [
    "Are you the nah id win because you're the strongest or are you the stand proud because you're the with this treasure I summon? Always bet on hakari",
    "Are you strong because you Nah, I'd win, or did you leave it all behind and stand proud because with this treasure I summon always bet on Hakari. I'M YOU",
    "Are you the exception because you stand proud or do you stand proud because you are the exception?",
    """Is Jujutsu folk because they're Nah I'd Win? Or is Folk Jujutsu because With this treasure I summon JoGoat, who always bets on Hakari and with his Domain Expansion he says "I'm You" while bringing out 120% of their potential?""",
    "are you strong because that’s how losers think or did you leave it all behind because you always bet on hakari and his overwhelming intensity"
]

# Directories for media files
IMAGE_FOLDER = "jjk_images"
VIDEO_FOLDER = "jjk_videos"
for folder in [IMAGE_FOLDER, VIDEO_FOLDER]:
    if not os.path.exists(folder):
        os.makedirs(folder)

def get_random_file(folder, extensions):
    files = [f for f in os.listdir(folder) if f.endswith(extensions)]
    if not files:
        return None
    return os.path.join(folder, random.choice(files))

@app.route('/random', methods=['GET'])
def get_random_quote():
    return jsonify({"quote": random.choice(quotes)})

@app.route('/random-photo', methods=['GET'])
def get_random_photo():
    image_path = get_random_file(IMAGE_FOLDER, (".png", ".jpg", ".jpeg", ".webp"))
    if image_path:
        return send_file(image_path, mimetype='image/jpeg')
    return jsonify({"error": "No images available."}), 404

@app.route('/random-video', methods=['GET'])
def get_random_video():
    video_path = get_random_file(VIDEO_FOLDER, (".mp4", ".mov", ".avi"))
    if video_path:
        return send_file(video_path, mimetype='video/mp4')
    return jsonify({"error": "No videos available."}), 404

@app.route('/quote/<int:index>', methods=['GET'])
def get_specific_quote(index):
    if 0 <= index < len(quotes):
        return jsonify({"quote": quotes[index]})
    return jsonify({"error": "Index out of range."}), 404

@app.route('/add', methods=['POST'])
def add_quote():
    data = request.get_json()
    if not data or "quote" not in data:
        return jsonify({"error": "Invalid data. A 'quote' field is required."}), 400

    quotes.append(data["quote"])
    return jsonify({"message": "Quote added successfully!", "quote": data["quote"]}), 201

@app.route('/add-photo', methods=['POST'])
def add_photo():
    if 'photo' not in request.files:
        return jsonify({"error": "No photo file provided."}), 400

    file = request.files['photo']
    if file.filename == '':
        return jsonify({"error": "No selected file."}), 400

    file_path = os.path.join(IMAGE_FOLDER, file.filename)
    file.save(file_path)
    return jsonify({"message": "Photo added successfully!", "filename": file.filename}), 201

@app.route('/add-video', methods=['POST'])
def add_video():
    if 'video' not in request.files:
        return jsonify({"error": "No video file provided."}), 400

    file = request.files['video']
    if file.filename == '':
        return jsonify({"error": "No selected file."}), 400

    file_path = os.path.join(VIDEO_FOLDER, file.filename)
    file.save(file_path)
    return jsonify({"message": "Video added successfully!", "filename": file.filename}), 201

@app.route('/quotes-count', methods=['GET'])
def quotes_count():
    return jsonify({"total_quotes": len(quotes)})

@app.route('/photos-count', methods=['GET'])
def photos_count():
    images = [img for img in os.listdir(IMAGE_FOLDER) if img.endswith((".png", ".jpg", ".jpeg", ".webp"))]
    return jsonify({"total_photos": len(images)})

@app.route('/videos-count', methods=['GET'])
def videos_count():
    videos = [vid for vid in os.listdir(VIDEO_FOLDER) if vid.endswith((".mp4", ".mov", ".avi"))]
    return jsonify({"total_videos": len(videos)})

@app.route('/delete-photo/<filename>', methods=['DELETE'])
def delete_photo(filename):
    file_path = os.path.join(IMAGE_FOLDER, filename)
    if os.path.exists(file_path):
        os.remove(file_path)
        return jsonify({"message": "Photo deleted successfully!"}), 200
    return jsonify({"error": "File not found."}), 404

@app.route('/delete-video/<filename>', methods=['DELETE'])
def delete_video(filename):
    file_path = os.path.join(VIDEO_FOLDER, filename)
    if os.path.exists(file_path):
        os.remove(file_path)
        return jsonify({"message": "Video deleted successfully!"}), 200
    return jsonify({"error": "File not found."}), 404

@app.route('/delete-quote/<int:index>', methods=['DELETE'])
def delete_quote(index):
    if 0 <= index < len(quotes):
        removed_quote = quotes.pop(index)
        return jsonify({"message": "Quote deleted successfully!", "quote": removed_quote}), 200
    return jsonify({"error": "Index out of range."}), 404

if __name__ == '__main__':
    app.run(debug=True)
