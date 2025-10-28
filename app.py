import streamlit as st
from levels import init_levels
from player import Player

# Initialize session state
if "player" not in st.session_state:
    st.session_state.player = None
if "levels" not in st.session_state:
    st.session_state.levels = init_levels()

# --- FUNCTIONS ---
def start_new_game(name):
    st.session_state.player = Player(name=name)
    st.session_state.player.save()

def load_game():
    loaded = Player.load()
    if loaded:
        st.session_state.player = loaded
        return True
    return False

# --- PAGE TITLE ---
st.title("🎮 Gamified Learning – A Question-Driven Exploration Experience")

# --- START OR CONTINUE GAME ---
if not st.session_state.player:
    st.subheader("Start or Continue Your Game")
    name = st.text_input("Enter your name:")
    col1, col2 = st.columns(2)

    with col1:
        if st.button("Start New Game"):
            if name.strip():
                start_new_game(name)
                st.rerun()
            else:
                st.warning("Please enter a name first.")
    with col2:
        if st.button("Load Saved Game"):
            if not load_game():
                st.error("No saved progress found!")
else:
    # --- MAIN GAME SCREEN ---
    player = st.session_state.player
    levels = st.session_state.levels
    total_levels = len(levels)

    st.sidebar.header("📋 Player Status")
    st.sidebar.write(f"**Name:** {player.name}")
    st.sidebar.write(f"**Lives:** ❤️ {player.lives}")
    st.sidebar.write(f"**Level:** {player.current_level + 1} / {total_levels}")
    st.sidebar.write(f"**Badges:** {player.badges if player.badges else 'None'}")

    if player.lives <= 0:
        st.error("Game Over! You lost all lives 😢")
        if st.button("Restart Game"):
            st.session_state.player = None
            st.rerun()
    elif player.current_level >= total_levels:
        st.success(f"🎉 Congratulations {player.name}, you finished all levels!")
        st.balloons()
        if st.button("Play Again"):
            st.session_state.player = None
            st.rerun()
    else:
        level = levels[player.current_level]
        st.header(f"Level {player.current_level + 1}: {level['title']}")
        st.write(level["narrative"])

        q = level["question"]
        st.markdown(f"**{q['prompt']}**")
        choice = st.radio("Choose your answer:", q["choices"])

        col1, col2 = st.columns(2)
        with col1:
            if st.button("Submit"):
                selected_index = q["choices"].index(choice)
                if selected_index == q["answer"]:
                    st.success("✅ Correct Answer!")
                    badge = f"Badge-{player.current_level + 1}"
                    if badge not in player.badges:
                        player.badges.append(badge)
                    player.current_level += 1
                    player.save()
                    st.rerun()
                else:
                    st.error("❌ Wrong Answer! You lost one life.")
                    player.lives -= 1
                    player.save()
                    st.rerun()
        with col2:
            if st.button("Hint"):
                st.info(q.get("hint", "No hint available."))

        st.button("💾 Save Progress", on_click=player.save)
