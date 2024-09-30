import os

def find_improperly_quoted_paths(file_content):
	improper_paths = []
	lines_enum = enumerate(file_content.splitlines(), start=1)
	lines = list(lines_enum)
	
	# Go through each line in the file
	for line_num, line in lines:
		start_quote = None
		potential_path = ""

		# Scan through each character in the line
		for i, char in enumerate(line):
			# Detect a starting quote (single or double)
			if char in ["'", '"']:
				# If there's no start quote yet, mark this as the starting quote
				if start_quote is None:
					start_quote = char
					potential_path = char  # Start tracking the path
				# If there's a closing quote that matches the start quote, reset
				elif char == start_quote:
					start_quote = None
					potential_path = ""  # Reset because the quote was properly closed
				else:
					potential_path += char
			elif start_quote is not None:
				# Accumulate characters inside the quotes
				potential_path += char

		# After looping through a line, check if the line has an unclosed quote and return the line.
		if start_quote is not None:
			improper_paths.append((line_num, line))
			
	return improper_paths



def process_files_in_directory(directory):
	# Iterate over all files in the directory
	for root, _, files in os.walk(directory):
		for filename in files:
			if filename.endswith(".js") or filename.endswith(".html") or filename.endswith(".txt"):  # Add file extensions as needed
				file_path = os.path.join(root, filename)
				with open(file_path, 'r', encoding='utf-8') as file:
					file_content = file.read()

				# Find improperly quoted paths in the file
				improper_paths = find_improperly_quoted_paths(file_content)
				
				if improper_paths:
					print(f"File: {file_path}")
					for line_num, path in improper_paths:
						print(f"  Line {line_num}: {path}")
					print()


if __name__ == "__main__":
	# Specify the directory you want to scan
	directory_to_scan = input('Path (will process all files in path):\n')

	
	# Process all files in the directory
	process_files_in_directory(directory_to_scan)
