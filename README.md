# Blog Templating

This is a simple blogging application built with Flask. It retrieves blog posts from an API and displays them on a web page. Users can click on a blog post to view its full content.

## Features

- Fetches blog posts from a remote API
- Displays a list of blog posts on the home page
- Allows users to click on a blog post to view its full content

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/MirelaManta/flask-blog-templating.git
   ```

2. Navigate to the project directory:

   ```bash
   cd flask-blog-templating
   ```

3. Install the required dependencies:

   ```bash
   pip install flask
   ```

4. Start the application:

   ```bash
   python main.py
   ```

5. Open a web browser and visit `http://localhost:5000` to access the blog.

## Technologies Used

- Python
- Flask
- HTML
- CSS

## API Endpoint

The application retrieves blog posts from the following API endpoint:

- API URL: `https://api.npoint.io/c790b4d5cab58020d391`

## File Structure

The project structure is as follows:

- `main.py`: The main Flask application file.
- `post.py`: Contains the `Post` class representing a blog post.
- `templates/index.html`: The HTML template for the home page, displaying the list of blog posts.
- `templates/post.html`: The HTML template for displaying a full blog post.
- `static/css/styles.css`: CSS styles for the application.
