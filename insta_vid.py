from instaloader import Instaloader, Post 
import os

def download_instagram_video(url, download_dir):
  """Downloads an Instagram video given the URL and saves it to the specified directory.

  Args:
    url: The URL of the Instagram video.
    download_dir: The path to the directory where the video should be saved.

  Raises:
    Exception: If there's an error downloading the video.
  """
  try:
    L = Instaloader()
    shortcode = url.split('/')[-2] 
    post = Post.from_shortcode(L.context, shortcode) 
    L.download_post(post, target=download_dir)
    print(f"Video downloaded successfully to: {download_dir}/{post.date_utc}_{post.shortcode}.mp4")
  except Exception as e:
    print(f"Error downloading video: {e}")

if __name__ == "__main__":
  url = input("Enter the Instagram video URL: ")
  download_dir = "videos"
  download_instagram_video(url, download_dir)