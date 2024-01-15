import re

html_text = '<tr align="right"><td>12</td><td>Andrew</td><td>Addison</td></tr>'

# Define the regular expression pattern
pattern = re.compile(r'<tr align="right"><td>(\d+)</td><td>(.*?)</td><td>(\w+)</td></tr>')

# Use the pattern to find matches in the HTML text
match = pattern.search(html_text)

# Extract the matched values
if match:
    value1 = match.group(1)
    value2 = match.group(2)
    value3 = match.group(3)

    print("Value 1:", value1)
    print("Value 2:", value2)
    print("Value 3:", value3)
else:
    print("No match found.")
