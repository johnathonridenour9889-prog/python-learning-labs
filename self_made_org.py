import os
import shutil

def _users_folder_():
    return input('Enter folder path you would like to organize:')

def _validate_path_():
    while True:

            chose = _users_folder_()

            if os.path.isdir(chose):
                return chose

            print('Please enter a valid folder path')

def _organizer_():
    valid = _validate_path_()

    for filenames in os.listdir(valid):
        full_path = os.path.join(valid, filenames)

        if not os.path.isfile(full_path):
            continue

        extens = os.path.splitext(filenames)[1].lower()

        if extens in ['.jpg', '.jpeg', '.png']:
            folder = 'Images'
        elif extens in ['.docx', '.txt', '.pdf','.cvs','.pub']:
            folder = 'Documents'
        elif extens in ['.mp4', '.mov']:
            folder = 'Videos'
        elif extens in ['.exe', '.bat', '.cmd', '.ps1', '.msi', '.com', '.scr','.vbs']:
            folder = 'Executables'
        elif extens in ['.py', '.js', '.html', '.css', '.json']:
            folder = 'Scripts'
        elif extens in ['.zip', '.rar', '.7z']:
            folder = 'Archives'
        elif extens in ['.mp3', '.wav', '.flac']:
            folder = 'Audio'
        elif extens in ['.iso']:
            folder = 'Iso'
        else:
            folder = 'other'

        dest = os.path.join(valid, folder)

        if not os.path.exists(dest):
            os.makedirs(dest)

        dest_path = os.path.join(dest, filenames)

        if os.path.exists(dest_path):
            print(f"{filenames} already exists, skipping")
            continue

        shutil.move(full_path, dest_path)

        print(f"{filenames} -> {folder}")

    print('Done organize was successfully completed')

def main():
    _organizer_()

if __name__ == '__main__':
    main()


