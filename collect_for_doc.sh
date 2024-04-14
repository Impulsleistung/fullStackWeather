#!/bin/bash

# Specify the output file
output_file="complete.txt"

# Clear the output file if it already exists
> "$output_file"

# Function to append file content with headers
function append_file_content {
    echo "File: $1" >> "$output_file"
    echo "Path: $2" >> "$output_file"
    echo "----------------------------------------" >> "$output_file"
    cat "$1" >> "$output_file"
    echo -e "\n\n" >> "$output_file"
}

# Find files with specified extensions and process each
find . -type f \( -name "*.csv" -o -name "*.js" -o -name "*.py" -o -name "*.html" -o -name "*.yaml" -o -name "*.md" -o -name "*.css" \) |
while IFS= read -r file; do
    append_file_content "$file" "$(dirname "$file")"
done

# Output the file tree
echo "File Tree:" >> "$output_file"
find . -print >> "$output_file"
