def extract_in_data(filepath):
  """
  Extracts lines containing 'IN' from the specified file path.

  Args:
      filepath: Path to the text file.

  Returns:
      A list of lines containing 'IN'.
  """
  in_data = []
  with open(filepath, 'r') as f:
    for line in f:
      if 'IN' in line:
        in_data.append(line.strip())
  return in_data

def visualize_data(data):
  """
  Visualizes the extracted data in a table format (using print).

  Args:
      data: List of lines containing 'IN'.
  """
  print("IN Regions Data:")
  print("-" * 20)
  for line in data:
    print(line)

# Replace with your actual file path
filepath = "/workspaces/AdiFiles/S.txt"

in_data = extract_in_data(filepath)
visualize_data(in_data)




   
