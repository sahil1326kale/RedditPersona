# Reddit Persona Generator 🧠

This Python script generates a **User Persona** by analyzing a Reddit user's public posts and comments.

## 🚀 What It Does

- Takes a Reddit username as input.
- Scrapes the user's **latest posts and comments** using Reddit API.
- Generates a simple **user persona** based on their activity.
- Outputs the persona in a `.txt` file inside the `output/` folder.
- Cites the exact post/comment URLs used.

---

## 📦 Requirements

Install Python libraries:

```bash
pip install praw

🛠 How to Use
1-Clone this repo:
git clone https://github.com/yourusername/RedditPersona.git
cd RedditPersona

2-Create a file named reddit_config.py with your Reddit credentials:
REDDIT_CLIENT_ID = "your_client_id"
REDDIT_CLIENT_SECRET = "your_client_secret"
REDDIT_USERNAME = "your_reddit_username"
REDDIT_PASSWORD = "your_reddit_password"
REDDIT_USER_AGENT = "PersonaScript by u/your_username"

3-Run the script:
python main.py

4-Enter a Reddit username when prompted (e.g. kojied)

5-The output will be saved in the output/ folder.
