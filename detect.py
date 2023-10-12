import copy_move_detection.image_object
from pathlib import Path

def detect(input_path, output_path, block_size=16):


    input_path = Path(input_path)
    filename = input_path.name
    output_path= Path(output_path)

    if not input_path.exists():
        print("Error: Source Directory did not exist.")
        exit(1)
    elif not output_path.exists():
        print("Error: Output Directory did not exist.")
        exit(1)

    single_image = copy_move_detection.image_object.ImageObject(input_path, filename, output_path, block_size)
    image_result_path = single_image.run()

    print("Done.")
    return image_result_path
