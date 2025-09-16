# import gradio as gr
# import subprocess

# def run_simulation():
#     # run the original simulation script
#     subprocess.run(["python", "simulation.py"])
#     return "Simulation finished (check logs)."

# demo = gr.Interface(fn=run_simulation, inputs=None, outputs="text")
# demo.launch()
# app.py
import gradio as gr
from simulation import generate_frames  # or a Simulation class you made
from PIL import Image

def stream_simulation():
    # generator that yields PIL Images — Gradio can stream images
    for img in generate_frames(num_frames=400):
        yield img

demo = gr.Interface(fn=stream_simulation, inputs=None, outputs=gr.Image(type="pil"))
# Spaces requires server_name and port handled by Gradio; this will be fine in HF
demo.launch()
