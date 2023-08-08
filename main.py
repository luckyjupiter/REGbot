import telebot
import win32com.client
import pythoncom
import openai

# Set your OpenAI API key here
OPENAI_API_KEY = "openai_key"
openai.api_key = OPENAI_API_KEY

TOKEN = "telegram_key"
bot = telebot.TeleBot(TOKEN)
chats = {}

# Define the positive random tasks
positive_tasks = [
       "Write a short story about a magical adventure.",
    "Create a new recipe and cook a delicious meal.",
    "Paint a picture of a beautiful landscape.",
    "Learn to play a musical instrument.",
    "Write a heartfelt letter to someone you care about.",
    "Start a journal and write about your day.",
    "Take a nature walk and observe the wildlife.",
    "Try a new sport or physical activity.",
    "Volunteer at a local charity or community event.",
    "Visit a museum or art gallery and appreciate the exhibits.",
    "Organize a game night with friends or family.",
    "Plant a garden and grow your favorite flowers or vegetables.",
    "Write a poem expressing your emotions.",
    "Learn a new language or practice speaking one you know.",
    "Start a DIY project and create something unique.",
    "Watch a classic movie or a feel-good comedy.",
    "Visit a local park and have a picnic.",
    "Read a book that inspires you.",
    "Practice yoga or meditation for relaxation.",
    "Donate clothes or items to those in need.",
    "Write a list of things you are grateful for.",
    "Take photos of beautiful sights in your city.",
    "Try a new hobby or craft.",
    "Reach out to an old friend and reconnect.",
    "Create a vision board for your goals.",
    "Write a positive affirmation and repeat it daily.",
    "Cook a meal for a friend or family member.",
    "Explore a nearby town or city you haven't visited before.",
    "Make a playlist of your favorite songs.",
    "Do a random act of kindness for a stranger.",
    "Visit a local farmer's market and try new foods.",
    "Host a virtual movie night with friends.",
    "Take a digital detox day and spend time offline.",
    "Learn to dance a new style or dance move.",
    "Write a thank-you note to someone who made a difference in your life.",
    "Start a fitness challenge and set achievable goals.",
    "Create a scrapbook of cherished memories.",
    "Volunteer at an animal shelter and spend time with pets.",
    "Try a new coffee shop or restaurant in your area.",
    "Practice deep breathing exercises for relaxation.",
    "Organize a virtual book club and discuss your favorite books.",
    "Write a letter to your future self with your aspirations.",
    "Watch the sunrise or sunset and appreciate the beauty of nature.",
    "Learn a magic trick and amaze your friends.",
    "Take a day trip to a nearby beach or lake.",
    "Host a virtual talent show and showcase your skills.",
    "Write a list of positive affirmations for self-confidence.",
    "Volunteer for a beach or park cleanup event.",
    "Try a new type of cuisine or cooking style.",
    "Host a virtual game night with board games or online games.",
    "Learn to knit or crochet and make a cozy item.",
    "Write a blog post about a topic you are passionate about.",
    "Create a DIY gift for someone special in your life.",
    "Take a day to declutter and organize your living space.",
    "Try a new hairstyle or experiment with hair accessories.",
    "Watch a documentary on a topic that interests you.",
    "Do a puzzle or brain teaser to challenge yourself.",
    "Start a gratitude jar and add a note each day.",
    "Host a virtual art session and paint or draw together.",
    "Write a letter of appreciation to a teacher or mentor.",
    "Practice positive visualization for your goals.",
    "Visit a local botanical garden or nature reserve.",
    "Try a virtual escape room game with friends.",
    "Make a list of personal strengths and celebrate them.",
    "Learn a new skill through online tutorials or courses.",
    "Start a small herb garden on your windowsill.",
    "Create a playlist of motivational podcasts.",
    "Try a new ice cream or dessert flavor.",
    "Write a motivational quote and share it with others.",
    "Visit a local historical site or museum.",
    "Practice random acts of kindness throughout the day.",
    "Host a virtual cooking class and share your favorite recipe.",
    "Learn to juggle or try other circus skills.",
    "Write a letter of encouragement to your future self.",
    "Explore a nearby forest or nature trail.",
    "Try a new type of exercise or fitness class.",
    "Start a daily gratitude practice.",
    "Create a time capsule with items from this year.",
    "Host a virtual karaoke night and sing your favorite songs.",
    "Write a short play or skit and perform it with friends.",
    "Practice positive self-talk and affirmations.",
    "Learn to make homemade candles or soap.",
    "Volunteer at a local food bank or soup kitchen.",
    "Try a new type of dance or dance workout.",
    "Write a list of dreams and aspirations for the future.",
    "Host a virtual trivia night with friends.",
    "Learn to make origami or paper crafts.",
    "Start a virtual book exchange with friends.",
    "Visit a local art studio or gallery.",
    "Try a new type of tea or coffee blend.",
    "Write a letter to your favorite author or artist.",
    "Practice mindfulness while enjoying a cup of tea or coffee.",
    "Learn to make homemade pizza or pasta.",
    "Visit a local zoo or animal sanctuary.",
    "Try a virtual escape room game with friends.",
    "Write a letter to your future self with your dreams and goals.",
    "Explore a nearby city and be a tourist for the day.",
    "Start a virtual workout challenge with friends.",
    "Learn to do calligraphy or hand lettering.",
    "Write a list of positive affirmations for daily motivation.",
    "Host a virtual dance party and invite friends to join.",
    "Learn to make homemade ice cream or popsicles.",
    "Volunteer for a beach or park cleanup event.",
    "Try a new type of cuisine or cooking style.",
    "Host a virtual game night with board games or online games.",
    "Learn to knit or crochet and make a cozy item.",
    "Write a blog post about a topic you are passionate about.",
    "Create a DIY gift for someone special in your life.",
    "Take a day to declutter and organize your living space.",
    "Try a new hairstyle or experiment with hair accessories.",
    "Watch a documentary on a topic that interests you.",
    "Do a puzzle or brain teaser to challenge yourself.",
    "Start a gratitude jar and add a note each day.",
    "Host a virtual art session and paint or draw together.",
    "Write a letter of appreciation to a teacher or mentor.",
    "Practice positive visualization for your goals.",
    "Visit a local botanical garden or nature reserve.",
    "Try a virtual escape room game with friends.",
    "Make a list of personal strengths and celebrate them.",
    "Learn a new skill through online tutorials or courses.",
    "Start a small herb garden on your windowsill.",
    "Create a playlist of motivational podcasts.",
    "Try a new ice cream or dessert flavor.",
    "Write a motivational quote and share it with others.",
    "Visit a local historical site or museum.",
    "Practice random acts of kindness throughout the day.",
    "Host a virtual cooking class and share your favorite recipe.",
    "Learn to juggle or try other circus skills.",
    "Write a letter of encouragement to your future self.",
    "Explore a nearby forest or nature trail.",
    "Try a new type of exercise or fitness class.",
    "Start a daily gratitude practice.",
    "Create a time capsule with items from this year.",
    "Host a virtual karaoke night and sing your favorite songs.",
    "Write a short play or skit and perform it with friends.",
    "Practice positive self-talk and affirmations.",
    "Learn to make homemade candles or soap.",
    "Volunteer at a local food bank or soup kitchen.",
    "Try a new type of dance or dance workout.",
    "Write a list of dreams and aspirations for the future.",
    "Host a virtual trivia night with friends.",
    "Learn to make origami or paper crafts.",
    "Start a virtual book exchange with friends.",
    "Visit a local art studio or gallery.",
    "Try a new type of tea or coffee blend.",
    "Write a letter to your favorite author or artist.",
    "Practice mindfulness while enjoying a cup of tea or coffee.",
    "Learn to make homemade pizza or pasta.",
    "Visit a local zoo or animal sanctuary.",
    "Try a virtual escape room game with friends.",
    "Write a letter to your future self with your dreams and goals.",
    "Explore a nearby city and be a tourist for the day.",
    "Start a virtual workout challenge with friends.",
    "Learn to do calligraphy or hand lettering.",
    "Write a list of positive affirmations for daily motivation.",
    "Host a virtual dance party and invite friends to join.",
    "Learn to make homemade ice cream or popsicles.",
    "Volunteer for a local environmental conservation project.",
    "Try a new type of art or craft.",
    "Write a thank-you letter to a healthcare worker or first responder.",
    "Take a virtual tour of a famous landmark or museum.",
    "Practice positive thinking and focus on solutions.",
    "Start a virtual book club with friends or colleagues.",
    "Learn to make homemade bread or pastries.",
    "Volunteer at a local senior center or nursing home.",
    "Try a new form of exercise, such as pilates or dance aerobics.",
    "Write a letter to your future self with advice and encouragement.",
    "Visit a local farmer's market and support local vendors.",
    "Practice relaxation techniques, such as progressive muscle relaxation.",
    "Host a virtual talent show for friends or family members.",
    "Learn to make homemade natural beauty products.",
    "Write a letter to your past self and reflect on your journey.",
    "Start a virtual photography challenge and capture daily moments.",
    "Volunteer at a local shelter or community center.",
    "Try a virtual cooking class with a renowned chef.",
    "Practice positive affirmations for self-love and acceptance.",
    "Create a playlist of feel-good songs and share it with friends.",
    "Write a list of positive qualities about yourself.",
    "Host a virtual art workshop and teach others your skills.",
    "Learn to make homemade jewelry or accessories.",
    "Volunteer for a local environmental cleanup initiative.",
    "Try a new form of creative writing, such as poetry or haiku.",
    "Write a letter of appreciation to a mentor or role model.",
    "Start a virtual dance fitness class and invite friends to join.",
    "Explore a nearby hiking trail and connect with nature.",
    "Practice gratitude meditation to cultivate a thankful mindset.",
    "Host a virtual game tournament and award fun prizes.",
    "Learn to make homemade bath bombs or bath salts.",
    "Volunteer at a community garden or urban farming project.",
    "Try a new form of art therapy, such as mandala coloring.",
    "Write a letter to your favorite musician or artist.",
    "Start a virtual gratitude circle with friends or colleagues.",
    "Learn to make homemade herbal teas or infusions.",
    "Volunteer at a local literacy program or tutoring center.",
    "Try a new form of dance, such as salsa or hip-hop.",
    "Write a list of inspiring books and share it with others.",
    "Host a virtual DIY craft party and create together.",
    "Learn to make homemade greeting cards or postcards.",
    "Volunteer for a local animal rescue or wildlife rehabilitation center.",
    "Try a virtual puzzle-solving game with friends.",
    "Write a letter to your future self with your hopes and dreams.",
    "Explore a nearby nature reserve and observe the wildlife.",
    "Practice a new form of relaxation, such as guided imagery.",
    "Start a virtual gratitude journal and write daily entries.",
    "Volunteer at a local community cleanup or beautification event.",
    "Try a new form of meditation, such as loving-kindness meditation.",
    "Write a list of positive actions you can take to make a difference.",
    "Host a virtual dance-off or dance party with friends."
]

def get_random_number():
    """Generate a random 32-bit integer using the quantum device."""
    pythoncom.CoInitialize()
    qng = win32com.client.Dispatch("QWQNG.QNG")
    rand32 = qng.RandInt32
    pythoncom.CoUninitialize()
    return rand32

def get_random_task():
    """Get a random positive task from the list."""
    random_index = get_random_number() % len(positive_tasks)
    return positive_tasks[random_index]

def expand_task_with_gpt(task):
    """Expand the task using GPT-3.5 turbo."""
    prompt = f"Task: {task}\n\nExpand on the task:"
    response = openai.Completion.create(
        engine="text-davinci-002",  # You can use "text-davinci-002" or any other GPT-3.5 engine
        prompt=prompt,
        max_tokens=150
    )
    return response['choices'][0]['text'].strip()

@bot.message_handler(commands=['generate_task'])
def handle_generate_task(message):
    chat_id = message.chat.id
    random_task = get_random_task()
    expanded_task = expand_task_with_gpt(random_task)
    bot.send_message(chat_id, f"Your random positive task is:\n{random_task}\n\nExpanded task:\n{expanded_task}")

@bot.message_handler(func=lambda message: message.entities is not None and any(entity.type == 'mention' for entity in message.entities))
def handle_mention(message):
    chat_id = message.chat.id
    random_task = get_random_task()
    expanded_task = expand_task_with_gpt(random_task)
    bot.send_message(chat_id, f"{message.from_user.first_name}, here's a random positive task for you:\n{random_task}\n\nExpanded task:\n{expanded_task}")

# Polling loop to keep the bot running
bot.polling(none_stop=True)
