import os
import shutil


def _user_folder():
    return input("Enter folder path: ")


def _validate_path():
    while True:
        path = _user_folder()

        if os.path.isdir(path):
            return path

        print("Invalid folder path. Try again.")


def _organizer():
    valid = _validate_path()

    for file in os.listdir(valid):
        full_path = os.path.join(valid, file)

        if not os.path.isfile(full_path):
            continue

        extension = os.path.splitext(file)[1].lower()

        if extension in [".jpg", ".png", ".jpeg"]:
            folder_name = "Images"
        elif extension in [".pdf", ".txt", ".docx"]:
            folder_name = "Documents"
        elif extension in [".mp4", ".mov"]:
            folder_name = "Videos"
        else:
            folder_name = "Other"

        destination_folder = os.path.join(valid, folder_name)

        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

        destination_path = os.path.join(destination_folder, file)
        shutil.move(full_path, destination_path)

    print("Files organized.")


def main():
    _organizer()


if __name__ == "__main__":
    main()