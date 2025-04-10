import gradio as gr

def Bmi_Cal(name,height,weight):
    bmi = weight / ((height/3.28084) ** 2)
    result_Bmi="Hello, "+ name +" your BMI is: "+str(bmi)
    return result_Bmi

app = gr.Interface(fn=Bmi_Cal,inputs=("text",gr.Slider(0,8,0.1),gr.Slider(0,150)),outputs="text")
app.launch()