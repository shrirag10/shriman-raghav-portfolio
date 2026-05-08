import glob

files = glob.glob("*.html")
for f in files:
    with open(f, "r", encoding="utf-8") as file:
        content = file.read()
    
    if "G-XXXXXXXXXX" in content:
        content = content.replace("G-XXXXXXXXXX", "G-J4THJSZZJP")
        with open(f, "w", encoding="utf-8") as file:
            file.write(content)
        print(f"Updated GA ID in {f}")
