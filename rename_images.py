import os
import re
from natsort import natsorted


def get_unique_filename(base_name, ext):
    counter = 1
    new_name = f"{base_name}{ext}"
    while os.path.exists(new_name):
        new_name = f"{base_name}_{counter}{ext}"
        counter += 1
    return new_name


def rename_images():
    current_dir = os.getcwd()

    image_extensions = (".png", ".jpg", ".jpeg", ".gif", ".bmp")
    raw_image_files = [
        f for f in os.listdir(current_dir) if f.lower().endswith(image_extensions)
    ]
    image_files = natsorted(raw_image_files)

    for index, old_name in enumerate(image_files, start=1):
        _, ext = os.path.splitext(old_name)
        new_name = get_unique_filename(str(index), ext)
        os.rename(old_name, new_name)
        print(f"Renamed: {old_name} -> {new_name}")

    print("First round of renaming complete!")

    image_files = [
        f for f in os.listdir(current_dir) if f.lower().endswith(image_extensions)
    ]
    need_second_rename = any("_" in f for f in image_files)

    if need_second_rename:
        print("Detected files with suffixes. Starting second round of renaming...")
        image_files.sort(key=lambda f: int(re.split(r"_|\.", f)[0]))

        for index, old_name in enumerate(image_files, start=1):
            _, ext = os.path.splitext(old_name)
            new_name = f"{index}{ext}"
            if old_name != new_name:
                os.rename(old_name, new_name)
                print(f"Renamed: {old_name} -> {new_name}")

        print("Second round of renaming complete!")
    else:
        print("No need for second renaming. All files are correctly named.")


if __name__ == "__main__":
    rename_images()
