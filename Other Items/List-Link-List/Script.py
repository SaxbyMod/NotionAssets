def convert_names_to_links(input_file, output_file):
    base_url = "https://github.com/SaxbyMod/NotionAssets/raw/main/Formats/Desaft's%20Mod%20(CTI)/Portraits/"

    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            name = line.strip().replace(' ', '%20')
            link = f"{base_url}{name}.png"
            outfile.write(link + '\n')

# Example usage:
input_file = 'Names.txt'
output_file = 'YourLinks.txt'
convert_names_to_links(input_file, output_file)