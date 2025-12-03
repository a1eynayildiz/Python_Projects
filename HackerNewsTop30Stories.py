import requests

def get_top_stories(limit=30):
    top_stories_url = "https://hacker-news.firebaseio.com/v0/topstories.json"
    response = requests.get(top_stories_url)
    story_ids = response.json()[:limit]  # ilk 30 elemanı bu şekilde alıyoruz

    stories = []
    for story_id in story_ids:
        story_url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
        story_response = requests.get(story_url)
        stories.append(story_response.json())
    return stories


top_stories = get_top_stories(30)
for i, story in enumerate(top_stories, 1):
    print(f"{i}. Title: {story.get('title', 'No title')}")  # Eğer title yoksa "No title" yazdır
    print(f"   URL: {story.get('url', 'N/A')}")  # Eğer url yoksa: 'N/A (not available)' yazdır
    print(f"   Score: {story.get('score', 'N/A')}")
    print("---")