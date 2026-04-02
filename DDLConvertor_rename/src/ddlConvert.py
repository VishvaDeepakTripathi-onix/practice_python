import re
# read the file 
file_path = "./src/inputfiles.sql"
File_out = "./src/inputfiles_out.sql"
Relace_int = {"int" :	"int64"}
Replace_char = {"char" :	"string"}
Replace_nvarchar = {"nvarchar" :	"string"}
Replace_varchar = {"varchar" :	"string"}
Replace_text = {"text" :	"string"}
Replace_char = {"xml":	"string"}
# regex need to impliemnt 
regrx_pattern ="[$&+,:;=?@#|'<>.-^*()%!]*([0-9])[$&+,:;=?@#|'<>.-^*()%!]"
regex_pattern_char = "([char])"
Replace_Size_unused = {"(1)" : " "}
Replace_unused = {"COLLATE SQL_Latin1_General_CP1_CI_AS" : " "}

# Open the file in read mode
with open(file_path, "r") as file:
    lines = file.read()

# Print each line
# for line in lines:
#     print(line.strip())  # strip() removes the newline character

#unused
for old_str, new_str in Replace_unused.items():
    lines = lines.replace(old_str, new_str)

lines = re.sub(regrx_pattern, "", lines)


# string compare case when replace 
for old_str, new_str in Relace_int.items():
    lines = lines.replace(old_str, new_str)
for old_str, new_str in Replace_nvarchar.items():
    lines = lines.replace(old_str, new_str)
for old_str, new_str in Replace_char.items():
        lines = lines.replace(old_str, new_str)
#lines = re.sub(regex_pattern_char, "string", lines)

# for old_str, new_str in Replace_varchar.items():
#     lines = lines.replace(old_str, new_str)
# #Replace_text
# for old_str, new_str in Replace_text.items():
#     lines = lines.replace(old_str, new_str)
# #Replace_char
# for old_str, new_str in Replace_char.items():
#     lines = lines.replace(old_str, new_str)



with open(File_out, "w") as file:
    file.write(lines)

print("Replacement completed.")