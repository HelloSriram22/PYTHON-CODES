
import pywhatkit as pw

txt = """I am an enthusiastic, self-motivated, reliable, responsible, and hard-working person. 
I am a mature team worker and adaptable to all challenging situations. I am able to work well both in a team environment as well as using my own initiative. 
I am able to work well under pressure and adhere to strict deadlines. 
I enjoy overcoming challenges, and I have a genuine interest in Business Management."""

pw.text_to_handwriting(txt, "text_of_Ram.png", (255, 0, 0))
print("END")
