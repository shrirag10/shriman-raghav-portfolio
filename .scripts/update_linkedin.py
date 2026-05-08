import os
import re
import feedparser
from datetime import datetime
from dateutil import parser as date_parser
from bs4 import BeautifulSoup

def generate_post_html(post):
    """Generate the HTML block for a single post."""
    # Check if it's a WIP Wednesday post
    is_wip = "wip wednesday" in post.title.lower() or "wip wednesday" in post.description.lower()
    
    # Extract text from HTML description if present
    soup = BeautifulSoup(post.description, 'html.parser')
    text_content = soup.get_text(separator=' ', strip=True)
    
    # Truncate to ~250 chars for preview
    preview = text_content[:250] + "..." if len(text_content) > 250 else text_content
    
    date_str = post.published
    try:
        dt = date_parser.parse(date_str)
        formatted_date = dt.strftime("%b %d, %Y")
    except:
        formatted_date = date_str

    tag_html = ""
    if is_wip:
        tag_html = """<div class="inline-block px-3 py-1 rounded-full text-xs font-bold mb-3" style="background-color: var(--primary); color: var(--on-primary);">WIP Wednesday</div>"""
        
    return f"""
          <a href="{post.link}" target="_blank" class="glass-card rounded-2xl p-6 flex flex-col gap-4 block hover:-translate-y-1 transition-transform">
            {tag_html}
            <div class="text-xs font-space uppercase" style="color: var(--on-surface-variant);">{formatted_date}</div>
            <div class="text-sm" style="color: var(--on-surface); line-height: 1.6;">
              {preview}
            </div>
            <div class="mt-auto text-xs font-bold font-space flex items-center gap-2" style="color: var(--primary);">
              READ POST <span class="material-symbols-outlined text-sm">arrow_forward</span>
            </div>
          </a>"""

def main():
    rss_url = os.environ.get("LINKEDIN_RSS_URL")
    if not rss_url:
        print("Error: LINKEDIN_RSS_URL environment variable is missing.")
        return

    print(f"Fetching RSS feed from: {rss_url}")
    feed = feedparser.parse(rss_url)
    
    if feed.bozo:
        print("Warning: Feed parser reported bozo exception (might be malformed XML, but proceeding).")

    original_posts = []
    
    for entry in feed.entries:
        title = entry.get('title', '').lower()
        desc = entry.get('description', '').lower()
        
        # Filtering logic
        if "liked this" in title or "commented on" in title or "replied to" in title:
            continue
        if "liked this" in desc or "commented on" in desc or "replied to" in desc:
            continue
            
        original_posts.append(entry)

    print(f"Total entries: {len(feed.entries)} | Filtered Original Posts: {len(original_posts)}")
    
    if not original_posts:
        print("No original posts found to update.")
        return

    # Generate HTML for the posts (limit to top 6 to keep it clean)
    posts_html = "\n".join(generate_post_html(p) for p in original_posts[:6])
    
    # Read index.html
    index_path = "index.html"
    try:
        with open(index_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: {index_path} not found.")
        return

    # Replace content between markers
    start_marker = "<!-- LINKEDIN_POSTS_START -->"
    end_marker = "<!-- LINKEDIN_POSTS_END -->"
    
    pattern = re.compile(f"({start_marker}).*?({end_marker})", re.DOTALL)
    
    if not pattern.search(content):
        print(f"Error: Markers not found in {index_path}.")
        return
        
    new_content = pattern.sub(f"\\1\n{posts_html}\n        \\2", content)
    
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print("Successfully updated index.html with latest posts.")

if __name__ == "__main__":
    main()
