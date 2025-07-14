import praw
import os
from reddit_config import *

reddit = praw.Reddit(
    client_id=REDDIT_CLIENT_ID,
    client_secret=REDDIT_CLIENT_SECRET,
    username=REDDIT_USERNAME,
    password=REDDIT_PASSWORD,
    user_agent=REDDIT_USER_AGENT
)

def get_user_data(username):
    user = reddit.redditor(username)
    posts = []
    comments = []

    for post in user.submissions.new(limit=10):
        posts.append({"title": post.title, "body": post.selftext, "url": post.permalink})
    
    for comment in user.comments.new(limit=10):
        comments.append({"body": comment.body, "url": comment.permalink})

    return posts, comments

def create_persona(posts, comments):
    persona = "User Persona:\n"
    if posts:
        persona += f"- This user often posts about: {posts[0]['title'][:50]}\n"
        persona += f"  (Source: reddit.com{posts[0]['url']})\n"
    if comments:
        persona += f"- A sample comment: \"{comments[0]['body'][:50]}...\"\n"
        persona += f"  (Source: reddit.com{comments[0]['url']})\n"
    return persona

def save_to_file(username, persona):
    if not os.path.exists("output"):
        os.mkdir("output")
    with open(f"output/{username}_persona.txt", "w", encoding="utf-8") as f:
        f.write(persona)
    print(f"Saved to output/{username}_persona.txt")

if __name__ == "__main__":
    uname = input("Enter Reddit username (e.g. kojied): ")
    posts, comments = get_user_data(uname)
    persona = create_persona(posts, comments)
    save_to_file(uname, persona)
