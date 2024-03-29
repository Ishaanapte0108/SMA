import instaloader
import json
from instaloader import PostLocation as pl
# Create an instance of Instaloader with session
loader = instaloader.Instaloader()
loader.login('username', 'password')

profile = instaloader.Profile.from_username(loader.context, "louiscole")

posts_data = []
count = 0

for post in profile.get_posts():
    # Check if we have collected data for 2 posts
    print(f'count {count}')
    if count >= 100:
        break 

    post_data = {
        "type": post.typename,
        "post_url": f"https://www.instagram.com/p/{post.shortcode}/",
        "img_url": post.url,  
        "hashtags" : post.caption_hashtags,
        "timestamp": str(post.date_utc),
        "is_sponsored" : post.is_sponsored,
        "tagged_users" : post.tagged_users,
        "caption": post.pcaption,
        "child_posts" : post.comments,
        "caption" : post.caption,
        "likes_count" : post.likes,
        "video_view_count" : post.video_view_count if post.is_video else None,
        "video_duration" : post.video_duration if post.is_video else None,
        # "comments": post.comments
    }

    # Appending the dictionary to the list
    posts_data.append(post_data)
    count+=1

# Define the file path to save the JSON data
file_path = "data.json"

# Write the JSON data to the file
with open(file_path, "w") as json_file:
    json.dump(posts_data, json_file, indent=4)

print(f"Data saved to {file_path}")

