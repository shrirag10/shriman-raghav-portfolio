import os
import glob

meta_tags = """
  <!-- Open Graph / Social Meta Tags -->
  <meta property="og:type" content="website" />
  <meta property="og:title" content="Shriman Raghav Srinivasan — Robotics &amp; Manufacturing Engineer" />
  <meta property="og:description" content="MS Robotics at Northeastern. Bridging autonomous systems and production-ready manufacturing. Incoming Manufacturing Engineer at Tesla Fremont." />
  <meta property="og:image" content="images/shriman_portfolio.png" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="Shriman Raghav Srinivasan — Robotics &amp; Manufacturing Engineer" />
  <meta name="twitter:description" content="MS Robotics at Northeastern. Bridging autonomous systems and production-ready manufacturing. Incoming Manufacturing Engineer at Tesla Fremont." />
  <meta name="twitter:image" content="images/shriman_portfolio.png" />
"""

html_files = glob.glob("*.html")

for file_path in html_files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    if "og:title" in content:
        print(f"Skipping {file_path}, already has meta tags.")
        continue
        
    # Inject after description
    if 'content="MS Robotics at Northeastern. Bridging autonomous systems and production-ready manufacturing. Incoming Manufacturing Engineer at Tesla Fremont." />' in content:
        target = 'content="MS Robotics at Northeastern. Bridging autonomous systems and production-ready manufacturing. Incoming Manufacturing Engineer at Tesla Fremont." />'
    elif 'name="description"' in content:
        # Just find the end of the description meta tag
        target = 'name="description"\n    content="MS Robotics at Northeastern. Bridging autonomous systems and production-ready manufacturing. Incoming Manufacturing Engineer at Tesla Fremont." />'
    else:
        target = '<title>Shriman Raghav Srinivasan — Robotics &amp; Manufacturing Engineer</title>'
        
    if target in content:
        new_content = content.replace(target, target + "\n" + meta_tags)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Added meta tags to {file_path}")
    else:
        # Fallback to appending before </head>
        new_content = content.replace("</head>", meta_tags + "\n</head>")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Added meta tags to {file_path} (fallback)")

print("Done.")
