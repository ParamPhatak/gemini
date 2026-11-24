from google import genai
from dotenv import load_dotenv
load_dotenv()

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash-lite",
    input="Hey who are you in one word"
)
print(interaction.output_text)