import gradio
import openai
openai.api_key = "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"

messages = [{"role": "system", "content": 'NATURAL LANGUAGE PROCESSING BASED CHAT BOT'}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Natural Language Processing based Chat emotion detection")

demo.launch(share=True)