
import cv2
import customtkinter as ctk
from PIL import Image, ImageTk
import threading

class CameraDashboard(ctk.CTk):
    def _init_(self):
        super()._init_()

        self.title("Camera Dashboard")
        self.geometry(f"{12000}x{5800}")
        # Create a frame for the video feed
        self.video_frame = ctk.CTkFrame(self, width=800, height=580)
        self.video_frame.pack(pady=20)

        # Create a label inside the frame to display the video
        self.video_label = ctk.CTkLabel(self.video_frame)
        self.video_label.pack()

        # Start the video capture
        self.cap = cv2.VideoCapture(0)
        self.update_video()

    def update_video(self):
        """Read from the camera and update the video label."""
        ret, frame = self.cap.read()
        if ret:
            # Convert the image to RGB (OpenCV uses BGR)
            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(cv2image)

            # Convert image for tkinter
            imgtk = ImageTk.PhotoImage(image=img)
            self.video_label.configure(image=imgtk)
            self.video_label.image = imgtk

        # Repeat every few milliseconds
        self.after(10, self.update_video)

    def on_closing(self, event=None):
        """Handle window closing."""
        self.cap.release()
        self.destroy()

if __name__ == "__main__":
    app = CameraDashboard()
    # app.protocol("WM_DELETE_WINDOW", app.on_closing)
    app.mainloop()
