from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, filedialog
from tkinter.constants import DISABLED, ACTIVE, FLAT
from PIL import Image, ImageDraw, ImageFont


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


# -------------------------------------- FUNCTIONS -----------------------------------


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def upload_file():
    global file_path
    global extension
    file_path = filedialog.askopenfilename()
    try:
        extension = file_path.split(".")[1]
    except Exception as e:
        print(e)


def add_watermark(download_button):
    global photo
    photo = Image.open(file_path)
    width, height = photo.size
    drawing = ImageDraw.Draw(photo)
    font = ImageFont.truetype("Verdana.ttf", 20)
    text = f"{entry.get().lstrip()}    "
    text_width, text_height = drawing.textsize(text, font)
    text_position = width - text_width, (height - text_height) - 50
    c_text = Image.new("RGB", (text_width, (text_height)), color="#000000")
    drawing = ImageDraw.Draw(c_text)
    drawing.text((0, 0), text, fill="#fff", font=font)
    c_text.putalpha(100)
    photo.paste(c_text, text_position, c_text)
    download_button.config(state=ACTIVE)


def get_save_path():
    file_path = filedialog.asksaveasfilename()
    photo.save(f"{file_path}.{extension}")


# ------------------------------------ WINDOW CONFIG ---------------------------------

window = Tk()
window.title("Watermarker")
window.geometry("945x604")
window.configure(bg="#F4F8FF")

canvas = Canvas(
    window,
    bg="#F4F8FF",
    height=604,
    width=472,
    bd=0,
    highlightthickness=0,
    relief="ridge",
)

# ------------------------------------ WIDGETS ---------------------------------------

# Left side background
canvas.place(x=0, y=0)
canvas.create_rectangle(0.0, 0.0, 945.0, 604.0, fill="#205CD2", outline="")

# Title
canvas.create_text(
    63.0,
    98.0,
    anchor="nw",
    text="WATERMARKER",
    fill="#FFFFFF",
    font=("Roboto Medium", 36 * -1),
)

# underscore
canvas.create_rectangle(
    63.38330078125,
    164.88546752929688,
    325.05731201171875,
    164.88546752929688,
    fill="#FFFFFF",
    outline="",
)


canvas.create_text(
    63.0,
    187.0,
    anchor="nw",
    text="""
1. Upload Image


2. Add Watermark Text


3. Click on 'Add Watermark'


4. Download the Final Image
    
    """,
    fill="#FFFFFF",
    font=("Roboto", 18 * -1),
)

# ---------------------------------- BUTTONS ---------------------------------------

# UPLOAD BUTTON
btn_img_upload = PhotoImage(file=relative_to_assets("button_1.png"))

btn_upload = Button(
    image=btn_img_upload,
    borderwidth=0,
    highlightthickness=3,
    command=lambda: upload_file(),
    relief="flat",
)
btn_upload.place(x=612.0, y=98.0, width=197.0, height=53.0)

# DOWNLOAD BUTTON
btn_download_img = PhotoImage(file=relative_to_assets("button_3.png"))

btn_download = Button(
    image=btn_download_img,
    bd=0,
    highlightthickness=3,
    borderwidth=0,
    command=lambda: get_save_path(),
    relief=FLAT,
    state=DISABLED,
)

btn_download.place(x=612.0, y=388.0, width=184.0, height=53.0)

# ADD WATERMARK BUTTON
btn_add_watermark_img = PhotoImage(file=relative_to_assets("button_2.png"))

btn_add_watermark = Button(
    image=btn_add_watermark_img,
    borderwidth=0,
    highlightthickness=3,
    command=lambda: add_watermark(btn_download),
    relief="flat",
)

btn_add_watermark.place(x=581.0, y=277.0, width=240.0, height=53.0)

# --------------------------------- ENTRY BOX --------------------------------
entry = Entry(bd=0, bg="#FFFFFF", highlightthickness=0, font=("Helvetica", 20))
entry.insert(0, "    ")
entry.place(x=555.0, y=173.0, width=305.0, height=59.0)


window.resizable(False, False)
window.mainloop()
