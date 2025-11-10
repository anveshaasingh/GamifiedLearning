import streamlit as st
import random
from levels import init_levels
from player import Player
from leaderboard import get_top_players

# --- PAGE CONFIG ---
st.set_page_config(page_title="Gamified Learning", page_icon="🎮", layout="wide")

# --- CUSTOM THEME / HEADER ---
st.markdown(
    """
    <style>
    .main {
        background-color: #f7f9fc;
        color: #222;
        font-family: "Trebuchet MS", sans-serif;
    }
    .stButton>button {
        border-radius: 10px;
        height: 3em;
        width: 100%;
        font-weight: 600;
        background-color: #5b8def;
        color: white;
        border: none;
    }
    .stButton>button:hover {
        background-color: #4174d9;
        color: #fff;
    }
    .title {
        text-align: center;
        color: #3b3b98;
        font-size: 2.2em;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    '<h1 class="title">🎮 Gamified Learning – A Question-Driven Exploration Experience</h1>',
    unsafe_allow_html=True,
)
st.markdown("### Learn Programming Concepts Through Fun Quizzes 🚀")

# --- INITIALIZE SESSION STATE ---
if "player" not in st.session_state:
    st.session_state.player = None
if "levels" not in st.session_state:
    st.session_state.levels = init_levels()

# --- FUNCTIONS ---
def start_new_game(name):
    st.session_state.player = Player(name=name)
    st.session_state.player.save()


def load_game(name):
    loaded = Player.load(name)
    if loaded:
        if loaded.lives <= 0:
            loaded.lives = 3  # reset lives for retry
        st.session_state.player = loaded
        return True
    return False


# --- MAIN LOGIC ---
if not st.session_state.player:
    st.subheader("🧠 Start or Continue Your Game")
    name = st.text_input("Enter your name:")
    col1, col2 = st.columns(2)

    with col1:
        if st.button("Start New Game 🎯"):
            if name.strip():
                start_new_game(name)
                st.rerun()
            else:
                st.warning("Please enter your name first.")
    with col2:
        if st.button("Load Saved Game 💾"):
            if not load_game(name):
                st.error("No saved progress found!")
else:
    # --- MAIN GAME SCREEN ---
    player = st.session_state.player
    levels = st.session_state.levels
    total_levels = len(levels)

    # SIDEBAR SECTION
    st.sidebar.header("📋 Player Status")
    st.sidebar.success(f"👤 **Name:** {player.name}")
    st.sidebar.info(f"❤️ **Lives:** {player.lives}")
    st.sidebar.warning(f"📈 **Level:** {player.current_level + 1} / {total_levels}")
    st.sidebar.info(f"🏅 **Badges:** {', '.join(player.badges) if player.badges else 'None'}")
    st.sidebar.write(f"⭐ **Score:** {player.score}")

    st.sidebar.markdown("---")
    st.sidebar.header("🏆 Leaderboard")
    top_players = get_top_players()
    if top_players:
        for i, (name, score) in enumerate(top_players, start=1):
            st.sidebar.write(f"{i}. {name} - {score} pts")
    else:
        st.sidebar.write("No scores yet.")

    # --- GAME STATES ---
    if player.lives <= 0:
        st.error("💀 Game Over! You lost all lives.")
        if st.button("🔁 Restart Game"):
            st.session_state.player = None
            st.rerun()

    elif player.current_level >= total_levels:
        st.balloons()
        st.success(f"🎉 Congratulations {player.name}! You’ve completed all levels! 🎯")
        if st.button("Play Again 🔁"):
            st.session_state.player = None
            st.rerun()

    else:
        level = levels[player.current_level]
        progress = int(((player.current_level) / total_levels) * 100)
        st.progress(progress)
        st.header(f"🏰 Level {player.current_level + 1}: {level['title']}")
        st.markdown(f"**{level['narrative']}**")

        q = level["question"]
        st.markdown(f"### ❓ {q['prompt']}")

        # ✅ Escape special characters for safe display in Streamlit
        def escape_special_chars(text):
            return (
                text.replace("&", "&amp;")
                .replace("<", "&lt;")
                .replace(">", "&gt;")
                .replace("*", "✱")   # Show visually instead of Markdown bold
                .replace("#", "＃")  # Replace with full-width symbol
                .replace("%", "％")  # Replace with full-width symbol
            )

        safe_choices = [escape_special_chars(c) for c in q["choices"]]

        # ✅ Display safely in radio buttons
        choice = st.radio(
            "Choose your answer:",
            safe_choices,
            index=None,
            key=f"level_{player.current_level}",
        )

        col1, col2, col3 = st.columns(3)

        with col1:
            if st.button("✅ Submit Answer"):
                if choice:
                    selected_index = safe_choices.index(choice)
                    if selected_index == q["answer"]:
                        st.success("Correct! 🎯")
                        badge = f"Badge-{player.current_level + 1}"
                        if badge not in player.badges:
                            player.badges.append(badge)
                        player.score += 10
                        player.current_level += 1
                        player.save()
                        st.rerun()
                    else:
                        st.error("❌ Wrong Answer! You lost one life.")
                        player.lives -= 1
                        player.save()
                        st.rerun()
                else:
                    st.warning("Please select an option first.")

        with col2:
            if st.button("💡 Show Hint"):
                st.info(q.get("hint", "No hint available."))

        with col3:
            if st.button("💾 Save Progress"):
                player.save()
                st.success("Progress saved successfully!")

