# 5) OS File Manager
#    - Ask user for a directory path.
#    - Automatically:
#         - Create a folder "backup" inside it if not exists.
#         - Copy all .txt files into "backup".
#         - Print summary: how many files copied.
#    - If directory invalid, retry until correct.


def os_file_manager():
  import os
  import shutil

  while True:
    dir_path = input("Enter a directory path: ")
    if os.path.isdir(dir_path):
      break
    else:
      print("Invalid directory. Please try again.")

  backup_path = os.path.join(dir_path, "backup")
  os.makedirs(backup_path, exist_ok=True)

  txt_files = [f for f in os.listdir(dir_path) if f.endswith('.txt') and os.path.isfile(os.path.join(dir_path, f))]
  for file_name in txt_files:
    shutil.copy2(os.path.join(dir_path, file_name), backup_path)

  print(f"Copied {len(txt_files)} .txt files to 'backup' folder.")
  