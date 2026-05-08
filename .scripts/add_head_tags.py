import glob

favicon_and_ga = """
  <!-- Favicon -->
  <link rel="icon" type="image/png" href="images/shri_logo.png" />

  <!-- Google tag (gtag.js) - Placeholder -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-XXXXXXXXXX');
  </script>
"""

files = glob.glob("*.html")
for f in files:
    with open(f, "r", encoding="utf-8") as file:
        content = file.read()
    
    if '<link rel="icon"' not in content:
        content = content.replace("</head>", favicon_and_ga + "</head>")
        with open(f, "w", encoding="utf-8") as file:
            file.write(content)
        print(f"Added favicon and GA to {f}")
