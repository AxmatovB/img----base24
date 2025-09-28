import base64
import os
def convert_to_base64(input_file, output_file):
    with open(input_file, "rb") as f:
        img_data = f.read()
    b64_str = base64.b64encode(img_data).decode("utf-8")
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(b64_str)
    print(f"✅'{output_file}' saved")
try:
    from google.colab import files
    print("Choose file:")
    uploaded = files.upload()
    for filename in uploaded.keys():
        out_file = filename + "_base64.txt"
        convert_to_base64(filename, out_file)
        files.download(out_file)
except ImportError:
    input_file = input("📂 Name: ").strip()
    if not os.path.exists(input_file):
        print("No file")
    else:
        out_file = os.path.splitext(input_file)[0] + "_base64.txt"
        convert_to_base64(input_file, out_file)
