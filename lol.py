


import openai
import tkinter as tk 

openai.api_key = "ENTER your api KEY"

def get_the_response(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message

#gui interface
def display_response():
    input_text = input_field.get()
    response = get_the_response(input_text)
    output_field.config(state='normal')
    output_field.insert(tk.END, response)
    output_field.delete(1.0, tk.END)
    output_field.config(state='disabled')

#main window
root = tk.Tk()
root.geometry("1200x500")
root.title("Rohan's  Chatbot")


#input field
input_field = tk.Entry(root, font=("Helvetica", 14))
input_field.pack(pady=50)

#submit button
submit_button = tk.Button(root, text="Submit", font=("Helvetica", 12), command=display_response)
submit_button.pack(pady=10)

#output field
output_field = tk.Text(root, font=("Helvetica", 11), state='disabled')
output_field.pack(pady=10)

#GUI event loop
root.mainloop()
