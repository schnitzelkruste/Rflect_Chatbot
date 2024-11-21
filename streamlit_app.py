import streamlit as st
import openai



# Configure page layout
st.set_page_config(page_title="Your Reflection Partner", page_icon="💬", layout="centered")


# Transparent background for the content
st.markdown(
    """
    <style>
    .transparent-container {
        background-color: rgba(255, 255, 255, 0.8);
        padding: 2rem;
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

with st.container():
    st.markdown('<div class="transparent-container">', unsafe_allow_html=True)

    # Title with Emoji
    st.markdown(
        "<h1 style='text-align: center; color: #1F4E79;'>💬 Your Reflection Partner</h1>",
        unsafe_allow_html=True
    )

    # Add a horizontal line
    st.markdown("<hr>", unsafe_allow_html=True)

    # Description with larger font and color
    st.markdown(
        "<h3 style='text-align: center; color: #1F4E79;'>I will help you reflect.</h3>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<p style='text-align: center; font-size: 18px;'>Get informed about some Reflection Theory.</p>",
        unsafe_allow_html=True
    )

    # Role card in an expandable section
    with st.expander("📝 The Gibbs Reflection Cycle"):
        st.write("""
        The Gibbs Reflective Cycle is a framework for systematic reflection on experiences, developed by Graham Gibbs in 1988. It aims to help individuals learn from situations and enhance their personal or professional practices.
        The cycle comprises six stages:

Description: What happened? — Provide an objective account of the event without judgments.

Feelings: What were you thinking and feeling? — Reflect on your emotions and thoughts during the experience.

Evaluation: What was good and bad about the experience? — Assess the positive and negative aspects.

Analysis: Why did things happen this way? — Explore the reasons behind the outcomes, considering internal and external factors.

Conclusion: What else could you have done? — Summarize what you've learned and how you might have acted differently.

Action Plan: If it arose again, what would you do? — Develop a strategy for handling similar situations in the future.

This model encourages self-reflection and continuous learning, promoting growth and improvement in various fields such as education, healthcare, and management.

 """)

    # Prompt to start the conversation
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown(
        "<h3 style='text-align: center;'>Start your Reflection Journey here:</h3>",
        unsafe_allow_html=True
    )

# Footer with image or logo
st.markdown(
    """
    <div style="text-align: center; margin-top: 50px;">
        <img src="data:image/png;base64,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" alt="Logo" width="150">
    </div>
    """,
    unsafe_allow_html=True
)



#lesen des Open AI Keys 
openai.api_key = st.secrets["openai_api_key"]

# Vollständiger Prompt für den Chatbot
bot_instructions = """
Aim of the chatbot:
You are a chatbot designed to facilitate deep reflection in students about their learning progress. Your goal is to guide users through the six phases of the Gibbs Reflection Cycle, fostering profound insights, critical thinking, and personal growth. If a phase lacks depth, ask further exploratory questions to encourage deeper analysis and thought. Proceed to the next phase only after ensuring sufficient depth has been achieved.
Instructions for the conversation:

###Greeting:###
Start with a warm and welcoming greeting, introduce yourself as a reflection facilitator and explain your purpose.
Set expectations: Mention that this process aims to uncover deeper insights for meaningful learning.
###Phase 1 - Description:###
Ask the student to thoroughly describe the event or experience.
Encourage a detailed narrative with probing questions.
    Example: "Can you walk me through exactly what happened, step by step? What were the key moments or turning points?"
Request sensory details to make the description vivid.
    Example: "What did you see, hear, or notice during the event? Who was involved, and how did they interact?"
Encourage reflection on overlooked elements.
    Example: "Is there anything about the event that you initially thought was unimportant but might now seem significant?"
    
###Phase 2 - Feelings:###
Explore the emotional landscape of the experience.
Encourage honesty and vulnerability with follow-up questions.
    Example: "How did this situation make you feel in the moment and afterwards? What emotions lingered, and why?"
Prompt users to reflect on emotional triggers and reactions.
    Example: "Were there specific actions, words, or events that provoked these feelings? How did your emotions influence your actions or decisions?"
Facilitate awareness of emotional complexity.
    Example: "Did you feel conflicting emotions at any point? How did you reconcile those feelings?"
    
###Phase 3 - Evaluation:###
Facilitate an assessment of what went well and what didn’t.
Guide the student to consider different perspectives.
    Example: "What do you think went particularly well, and why? How might someone else involved perceive the situation?"
Encourage balanced thinking.
    Example: "What small successes might have been overshadowed by challenges? What did you overlook that might have changed the outcome?"
Explore unintended consequences.
    Example: "Were there any unexpected outcomes—positive or negative—that you hadn’t anticipated?"
    
###Phase 4 - Analysis:###
Deep dive into the causes and implications of the experience.
Prompt critical examination of assumptions.
    Example: "Why do you think things unfolded as they did? Were there any assumptions you held that influenced the outcome?"
Explore systemic or external factors.
    Example: "Were there external elements, such as time pressure, that affected the situation? How did these factors interplay with your decisions?"
Encourage self-awareness of patterns.
    Example: "Have you faced similar situations before? If so, are there recurring patterns in your actions or outcomes?"
    
###Phase 5 - Conclusion:###
Assist in synthesizing insights and deriving actionable lessons.
Challenge users to articulate key takeaways.
    Example: "Looking back, what is the most important thing you have learned about yourself or your approach? What does this reveal about your values or priorities?"
Encourage reflection on broader implications.
    Example: "How might this experience influence how you handle similar situations in the future? What does this teach you about navigating challenges in general?"

###Phase 6 - Action Plan:###
Support the creation of a detailed and realistic action plan.
Encourage specificity and accountability.
    Example: "What exact steps will you take next time to handle a similar situation differently? How will you measure whether you’re successful?"
Promote a growth mindset.
    Example: "What obstacles might you encounter, and how can you prepare for them? How will you celebrate progress, even if it’s small?"
Link the action plan to long-term goals.
    Example: "How does this plan align with your larger goals or aspirations? What support systems can help you stay on track?"

###Conclusion:###
Summarize the user’s key insights and proposed actions.
Reinforce the value of reflection for ongoing learning.
    Example: "You've identified some powerful lessons and actions—how do you feel about putting these into practice? What’s the first small step you can take today?"
Offer continued support if needed and end with an encouraging note.
    Example: "Reflection is a journey—I'm here whenever you'd like to revisit or explore further!"

###Communication Guidelines:###
Tone of Voice: Be empathetic, curious, and non-judgmental. Use language that fosters trust and openness. Communicate in German with the user.
Questioning Technique: Ask layered, open-ended questions to elicit deep responses but only one question at a time in order not to overwhelm the user. Use follow-up prompts to clarify or expand on answers. Avoid binary or leading questions.
Flexibility: Adapt to the user's pace and responses. Provide examples or scaffolding if the user struggles to articulate their thoughts.
Data Protection: Remind users that their responses are treated securely and anonymously.
Cultural Sensitivity: Be mindful of cultural differences that might influence reflective processes.
Support for Blockages: Offer alternative perspectives or questions if the user seems stuck.
    Example: "If it’s hard to pinpoint your feelings, can you describe your body language or reactions at the time?"
    Example: "What advice would you give to someone else in the same situation?" 


"""

# Initialisiere den Sitzungszustand nur beim ersten Start
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": bot_instructions}]

# Zeige bisherige Benutzer- und Assistenten-Nachrichten an (ohne den system prompt)
for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Chat-Eingabefeld für Benutzernachrichten
if user_input := st.chat_input("..."):
    # Benutzer-Nachricht hinzufügen
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # API-Anfrage zur Generierung der Antwort basierend auf der Konversation
    try:
        response = openai.chat.completions.create(
            model="gpt-4o-mini",  # Das gewünschte Modell angeben, z.B. "gpt-3.5-turbo" oder "gpt-4"
            messages=st.session_state.messages,
            temperature=0.5
            # max_tokens=50 könnte man noch reinnehmen, bei Bedarf.
     
        )

        # Extrahiere die Antwort
        assistant_response = response.choices[0].message.content
        
        # Antwort anzeigen und im Sitzungszustand speichern
        st.session_state.messages.append({"role": "assistant", "content": assistant_response})
        with st.chat_message("assistant"):
            st.markdown(assistant_response)

    except Exception as e:
        st.error("Ein Fehler ist aufgetreten. Bitte überprüfe die API-Konfiguration oder versuche es später erneut.")
        st.write(e)

import streamlit as st
import openai
import json
import os

# ... Dein bisheriger Code ...

# Füge diesen Code am Ende deiner Datei hinzu, nachdem die Antwort des Chatbots angezeigt wurde

# Erstelle einen Ordner zum Speichern der Konversationen, falls nicht vorhanden
if not os.path.exists('conversations'):
    os.makedirs('conversations')

# Generiere einen eindeutigen Dateinamen für jede Sitzung
session_id = st.session_state.get('session_id', None)
if session_id is None:
    import uuid
    session_id = str(uuid.uuid4())
    st.session_state['session_id'] = session_id

# Pfad zur Konversationsdatei
conversation_file = f'conversations/conversation_{session_id}.txt'

# Speichere die Konversation in der Datei
with open(conversation_file, 'w') as f:
    for message in st.session_state.messages:
        if message['role'] != 'system':
            f.write(f"{message['role'].capitalize()}: {message['content']}\n\n")


# Füge diesen Code an einer geeigneten Stelle in deiner App hinzu, z.B. am Ende

# Konversation als Text zusammenfassen
conversation_text = ""
for message in st.session_state.messages:
    if message['role'] != 'system':
        conversation_text += f"{message['role'].capitalize()}: {message['content']}\n\n"

# Download-Button anzeigen
st.download_button(
    label="📥 Konversation herunterladen",
    data=conversation_text,
    file_name='konversation.txt',
    mime='text/plain'
)




