import gradio as gr
import subprocess

def run_simulation():
    # run the original simulation script
    subprocess.run(["python", "../simulation.py"])
    return "Simulation finished (check logs)."

demo = gr.Interface(fn=run_simulation, inputs=None, outputs="text")
demo.launch()
