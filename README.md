# Mini Blog Project

## Description
This is a mini blog project built with Django that allows users to create and view posts, leave comments, and display only their own comments and posts. The project includes a RESTful API for managing posts and comments.

## Features
- Create, read, update, and delete posts.
- Leave comments on posts.
- View only your own posts and comments.
- Admin interface for managing posts and comments.

## Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd mini_blog
   ```
3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage
1. Run the migrations:
   ```
   python manage.py migrate
   ```
2. Start the development server:
   ```
   python manage.py runserver
   ```
3. Access the API at `http://127.0.0.1:8000/api/`.

## API Endpoints
- **Posts**
  - `GET /api/posts/` - List all posts
  - `POST /api/posts/` - Create a new post
  - `GET /api/posts/{id}/` - Retrieve a specific post
  - `PUT /api/posts/{id}/` - Update a specific post
  - `DELETE /api/posts/{id}/` - Delete a specific post

- **Comments**
  - `GET /api/comments/` - List all comments
  - `POST /api/comments/` - Create a new comment
  - `GET /api/comments/{id}/` - Retrieve a specific comment
  - `PUT /api/comments/{id}/` - Update a specific comment
  - `DELETE /api/comments/{id}/` - Delete a specific comment

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License
This project is licensed under the MIT License.