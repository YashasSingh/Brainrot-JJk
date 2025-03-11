# Brainrot-JJk
# JJK Brainrot API Documentation

## Overview
The **JJK Brainrot API** is a Flask-based web service that provides random Jujutsu Kaisen quotes, images, and videos. Users can retrieve, add, and delete quotes, images, and videos.

## Base URL
```
ysingh.pythonanywhere.com
```

## Endpoints

### 1. Get a Random Quote
**Endpoint:**
```
GET /random
```
**Response:**
```json
{
    "quote": "Dying to win and risking death to win are completely different, Megumi."
}
```

### 2. Get a Specific Quote
**Endpoint:**
```
GET /quote/<index>
```
**Parameters:**
- `index` (int) – Index of the quote in the list.

**Response:**
```json
{
    "quote": "A lesson learned the hard way is a lesson never forgotten."
}
```

### 3. Get a Random Photo
**Endpoint:**
```
GET /random-photo
```
**Response:**
- Returns an image file in `.png`, `.jpg`, `.jpeg`, or `.webp` format.

### 4. Get a Random Video
**Endpoint:**
```
GET /random-video
```
**Response:**
- Returns a video file in `.mp4`, `.mov`, or `.avi` format.

### 5. Add a New Quote
**Endpoint:**
```
POST /add
```
**Request Body:**
```json
{
    "quote": "Cursed energy flows better when you're relaxed."
}
```
**Response:**
```json
{
    "message": "Quote added successfully!",
    "quote": "Cursed energy flows better when you're relaxed."
}
```

### 6. Add a Photo
**Endpoint:**
```
POST /add-photo
```
**Form Data:**
- `photo` (file) – An image file.

**Response:**
```json
{
    "message": "Photo added successfully!",
    "filename": "jjk_image.webp"
}
```

### 7. Add a Video
**Endpoint:**
```
POST /add-video
```
**Form Data:**
- `video` (file) – A video file.

**Response:**
```json
{
    "message": "Video added successfully!",
    "filename": "jjk_clip.mp4"
}
```

### 8. Get Total Quotes Count
**Endpoint:**
```
GET /quotes-count
```
**Response:**
```json
{
    "total_quotes": 5
}
```

### 9. Get Total Photos Count
**Endpoint:**
```
GET /photos-count
```
**Response:**
```json
{
    "total_photos": 3
}
```

### 10. Get Total Videos Count
**Endpoint:**
```
GET /videos-count
```
**Response:**
```json
{
    "total_videos": 2
}
```

### 11. Delete a Quote
**Endpoint:**
```
DELETE /delete-quote/<index>
```
**Response:**
```json
{
    "message": "Quote deleted successfully!",
    "quote": "A lesson learned the hard way is a lesson never forgotten."
}
```

### 12. Delete a Photo
**Endpoint:**
```
DELETE /delete-photo/<filename>
```
**Response:**
```json
{
    "message": "Photo deleted successfully!"
}
```

### 13. Delete a Video
**Endpoint:**
```
DELETE /delete-video/<filename>
```
**Response:**
```json
{
    "message": "Video deleted successfully!"
}
```

## Notes
- **Supported Image Formats:** `.png`, `.jpg`, `.jpeg`, `.webp`
- **Supported Video Formats:** `.mp4`, `.mov`, `.avi`
- **All requests and responses use JSON unless specified otherwise.**

