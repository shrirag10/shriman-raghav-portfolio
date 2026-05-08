import glob

files = glob.glob("*.html")
for f in files:
    with open(f, "r", encoding="utf-8") as file:
        content = file.read()
    
    # 1. Title/Meta tags replacements (Use pipe)
    content = content.replace(" — Shriman", " | Shriman")
    content = content.replace("Shriman Raghav Srinivasan — ", "Shriman Raghav Srinivasan | ")
    
    # 2. Date ranges and general text with spaces (Use hyphen)
    content = content.replace(" — ", " - ")
    
    # 3. Em dashes without spaces (Use spaced hyphen)
    content = content.replace("—", " - ")
    
    with open(f, "w", encoding="utf-8") as file:
        file.write(content)
    print(f"Removed em dashes in {f}")
