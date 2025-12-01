# this code doesn't count for now. will work for this in future.
# # update_md_counters.py

# # Path to your Markdown file
# md_file = "movies.md"

# # Read the original file
# with open(md_file, "r", encoding="utf-8") as file:
#     lines = file.readlines()

# updated_lines = []
# current_genre = ""
# counter = 0

# for line in lines:
#     # Check if line is a genre header (starts with ###)
#     if line.startswith("###"):
#         # If we were counting a genre, update its previous header
#         if current_genre:
#             updated_lines[-1] = f"{current_genre} (Total: {counter})\n"
#         current_genre = line.strip()  # store current genre
#         counter = 0  # reset counter for new genre
#         updated_lines.append(line)  # temporarily keep header
#     elif line.strip().startswith("➤"):
#         counter += 1
#         updated_lines.append(line)
#     else:
#         updated_lines.append(line)

# # Update last genre
# if current_genre:
#     updated_lines[-1] = f"{current_genre} (Total: {counter})\n"

# # Write back to the Markdown file
# with open(md_file, "w", encoding="utf-8") as file:
#     file.writelines(updated_lines)

# print("✅ Counters updated in the Markdown file!")
