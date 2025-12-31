import cv2
import numpy as np
import matplotlib.pyplot as plt
import os


def pencil_sketch(image_path, blur_kernel=21):
    """
    Convert an image to a pencil sketch effect.

    Args:
        image_path (str): Path to input image
        blur_kernel (int): Gaussian blur kernel size (must be odd)

    Returns:
        tuple: (original_rgb, sketch) or (None, None) if error
    """
    try:
        # Validate kernel size
        if blur_kernel % 2 == 0:
            raise ValueError("Kernel must be odd")

        # Step 1: Load image
        image = cv2.imread(image_path)
        if image is None:
            raise FileNotFoundError("Image not found or invalid format")

        # Convert BGR to RGB for display
        original_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Step 2: Convert to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Step 3: Invert grayscale
        inverted = 255 - gray

        # Step 4: Apply Gaussian blur
        blurred = cv2.GaussianBlur(inverted, (blur_kernel, blur_kernel), 0)

        # Step 5: Invert blurred image
        inverted_blur = 255 - blurred

        #Divide And Scale
        gray_f = gray.astype(np.float32)
        inv_blur_f = inverted_blur.astype(np.float32)

        # Dodge blend
        sketch = cv2.divide(gray_f, inv_blur_f + 1.0, scale=256)

        # Clip and convert back to uint8
        sketch = np.clip(sketch, 0, 255).astype(np.uint8)

        return original_rgb, sketch

    except Exception as e:
        print(f"[ERROR] {e}")
        return None, None


def display_result(original, sketch, save_path=None):
    """
    Display original and sketch side-by-side.

    Args:
        original: Original image (RGB)
        sketch: Sketch image (grayscale)
        save_path: Optional path to save the sketch
    """
    plt.figure(figsize=(10, 5))

    # Original image
    plt.subplot(1, 2, 1)
    plt.imshow(original)
    plt.title("Original Image")
    plt.axis("off")

    # Sketch image
    plt.subplot(1, 2, 2)
    plt.imshow(sketch, cmap="gray")
    plt.title("Pencil Sketch")
    plt.axis("off")

    plt.tight_layout()
    plt.show()

    # Save output if path provided
    if save_path:
        cv2.imwrite(save_path, sketch)
        print(f"[INFO] Sketch saved to: {save_path}")


def main():
    """Main function to run the pencil sketch converter."""
    image_path = input("Enter image path: ").strip()

    if not os.path.exists(image_path):
        print("[ERROR] File does not exist.")
        return

    try:
        blur_kernel = int(input("Enter blur kernel size (odd number, default 21): ") or 21)
    except ValueError:
        print("[ERROR] Invalid kernel size.")
        return

    original, sketch = pencil_sketch(image_path, blur_kernel)

    if original is None or sketch is None:
        print("[ERROR] Failed to process image.")
        return

    save_path = "sketch_output.jpg"
    display_result(original, sketch, save_path)


if __name__ == "__main__":
    main()
