import cv2
import os

def crop_image(input_folder, output_folder, new_size):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    index_start = len([f for f in os.listdir(output_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))])
    for index, image_file in enumerate(image_files):
        input_path = os.path.join(input_folder, image_file)

        image = cv2.imread(input_path)

        cropped_image = cv2.resize(image, (new_size, new_size))

        new_name = f'img_{index + index_start}'

        output_path = os.path.join(output_folder, f'{new_name}.jpg')
        cv2.imwrite(output_path, cropped_image)

def main():
    input_folder = r".\dataset\my_data\original_images"
    output_folder = r".\dataset\my_data\cropped"
    new_size = 800

    crop_image(input_folder, output_folder, new_size)

if __name__ == '__main__':
    main()