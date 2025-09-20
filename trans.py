import gradio as gr
import whisper as wh

def transcribe_audio(audio,Text):
    model = wh.load_model("tiny")
    result = model.transcribe(audio)
    if Text.strip()== "":
        raise gr.Error("write text of what you speak")
    else:
        return result["text"],Text

demo = gr.Interface(
                    fn=transcribe_audio,
                    inputs=(gr.Microphone(type="filepath" ,label="input_for_audio"),gr.Textbox()),
                    outputs=("text","text"),
                    article="This is the demo for audio transcription and It base on speech to text by recording the voice ,and it's converts in the text format",
                    title="voice transcription",
                    theme=gr.themes.Ocean(),
                    flagging_dir="data_set"
                    )

demo.launch(debug=True,share=True)
