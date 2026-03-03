import streamlit as st

st.set_page_config(
    page_title="For Annie",
    layout="centered",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;1,300;1,400&family=Lato:wght@300;400&display=swap');

html, body, [class*="css"] {
    font-family: 'Lato', sans-serif;
    font-weight: 300;
    color: #4a3f35;
}

.stApp {
    background: #fdf8f2;
    background-image:
        radial-gradient(ellipse at 20% 10%, rgba(255,220,200,0.18) 0%, transparent 55%),
        radial-gradient(ellipse at 80% 90%, rgba(240,200,210,0.18) 0%, transparent 55%);
}

[data-testid="stSidebar"] {
    background: #fff7f0 !important;
    border-right: 1px solid #f0e0d0;
}
[data-testid="stSidebar"] * {
    font-family: 'Lato', sans-serif !important;
    color: #5a4035 !important;
}
[data-testid="stSidebar"] .stRadio label {
    font-size: 0.92rem;
    letter-spacing: 0.03em;
    padding: 6px 0;
    cursor: pointer;
}

h1, h2, h3 {
    font-family: 'Cormorant Garamond', serif !important;
    font-weight: 400;
    color: #3d2b1f;
}

.hero-title {
    font-family: 'Cormorant Garamond', serif;
    font-size: 3.6rem;
    font-weight: 300;
    color: #3d2b1f;
    letter-spacing: 0.05em;
    line-height: 1.1;
    margin-bottom: 0.1rem;
}
.hero-subtitle {
    font-family: 'Lato', sans-serif;
    font-size: 0.9rem;
    font-weight: 300;
    color: #a07060;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    margin-top: 0;
}

.section-title {
    font-family: 'Cormorant Garamond', serif;
    font-size: 2rem;
    font-weight: 400;
    color: #3d2b1f;
    letter-spacing: 0.04em;
    margin-bottom: 0.25rem;
}
.section-label {
    font-size: 0.78rem;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: #c49a8a;
    margin-bottom: 1.4rem;
}

.soft-divider {
    border: none;
    border-top: 1px solid #e8d5c8;
    margin: 2rem 0;
}

.body-text {
    font-size: 1.05rem;
    line-height: 1.9;
    color: #5a4035;
    font-weight: 300;
}

.pull-quote {
    border-left: 2px solid #e8b4a4;
    padding: 0.6rem 1.4rem;
    margin: 1.8rem 0;
    font-family: 'Cormorant Garamond', serif;
    font-size: 1.3rem;
    font-style: italic;
    color: #7a4f3a;
    line-height: 1.5;
    background: rgba(255,235,225,0.35);
    border-radius: 0 6px 6px 0;
}

.memory-slot {
    background: #fff9f5;
    border-radius: 12px;
    border: 1px solid #f0ddd2;
    padding: 1.4rem 1.4rem 1rem 1.4rem;
    margin-bottom: 0.5rem;
}
.memory-slot-title {
    font-family: 'Cormorant Garamond', serif;
    font-size: 1.25rem;
    font-weight: 500;
    color: #4a2e22;
    margin-bottom: 0.25rem;
}
.memory-slot-desc {
    font-size: 0.85rem;
    color: #a07060;
    line-height: 1.55;
    margin-bottom: 0.6rem;
}
.memory-placeholder {
    background: linear-gradient(135deg, #fdeee8 0%, #f9e0d8 100%);
    border-radius: 8px;
    height: 155px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #c49a8a;
    font-size: 0.8rem;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    border: 1.5px dashed #e8b4a4;
}
.memory-caption {
    font-family: 'Cormorant Garamond', serif;
    font-style: italic;
    font-size: 0.95rem;
    color: #7a5045;
    text-align: center;
    margin-top: 0.5rem;
}

.pill {
    display: inline-block;
    background: rgba(232,180,164,0.25);
    border: 1px solid #e8b4a4;
    border-radius: 999px;
    padding: 3px 14px;
    font-size: 0.78rem;
    color: #a06050;
    letter-spacing: 0.08em;
    margin: 3px 3px;
}

.step-card {
    background: #fff9f5;
    border-radius: 10px;
    border: 1px solid #f0ddd2;
    padding: 1rem 1.4rem;
    margin-bottom: 0.7rem;
    display: flex;
    align-items: flex-start;
    gap: 0.9rem;
}
.step-number {
    font-family: 'Cormorant Garamond', serif;
    font-size: 1.6rem;
    font-weight: 300;
    color: #e8a898;
    line-height: 1;
    min-width: 28px;
}
.step-text {
    font-size: 0.95rem;
    color: #5a4035;
    line-height: 1.55;
    padding-top: 0.15rem;
}

.moment-bubble {
    background: linear-gradient(135deg, #fff5f0 0%, #fdeae2 100%);
    border-radius: 14px;
    padding: 1rem 1.2rem;
    border: 1px solid #f0ddd2;
    margin-bottom: 0.8rem;
    font-size: 0.95rem;
    color: #6a4035;
    line-height: 1.65;
}

.footer {
    text-align: center;
    font-size: 0.78rem;
    color: #c4a090;
    letter-spacing: 0.1em;
    margin-top: 3rem;
    padding-top: 1.5rem;
    border-top: 1px solid #f0e0d0;
}

@keyframes pageFade {
    from { opacity: 0; transform: translateY(10px); }
    to   { opacity: 1; transform: translateY(0); }
}
.page-wrapper { animation: pageFade 0.5s ease forwards; }
</style>
""", unsafe_allow_html=True)


with st.sidebar:
    st.markdown("""
    <div style='text-align:center; padding: 1.2rem 0 1rem 0;'>
        <div style='font-family:"Cormorant Garamond",serif; font-size:1.6rem; color:#3d2b1f; letter-spacing:0.06em;'>For Annie</div>
        <div style='font-size:0.72rem; color:#c49a8a; letter-spacing:0.15em; text-transform:uppercase; margin-top:3px;'>a small scrapbook</div>
    </div>
    <hr style='border:none; border-top:1px solid #f0ddd2; margin:0.5rem 0 1.2rem 0;'>
    """, unsafe_allow_html=True)

    page = st.radio(
        "nav",
        ["Welcome", "Appreciation", "Memories", "Small Moments", "Why This Exists", "Access"],
        label_visibility="collapsed",
    )

    st.markdown("""
    <div style='margin-top:2.5rem; text-align:center; font-size:0.75rem; color:#d0a898; letter-spacing:0.08em;'>
        made with care
    </div>
    """, unsafe_allow_html=True)


def page_header(label, title):
    st.markdown(
        f"<div class='page-wrapper'>"
        f"<div class='section-label'>{label}</div>"
        f"<div class='section-title'>{title}</div>"
        f"</div>",
        unsafe_allow_html=True
    )
    st.markdown("<hr class='soft-divider'>", unsafe_allow_html=True)

def body(text):
    st.markdown(f"<div class='body-text'>{text}</div>", unsafe_allow_html=True)

def quote(text):
    st.markdown(f"<div class='pull-quote'>{text}</div>", unsafe_allow_html=True)

def spacer(h=20):
    st.markdown(f"<div style='height:{h}px'></div>", unsafe_allow_html=True)

def memory_slot(key, title, desc):
    st.markdown(
        f"<div class='memory-slot'>"
        f"<div class='memory-slot-title'>{title}</div>"
        f"<div class='memory-slot-desc'>{desc}</div>"
        f"</div>",
        unsafe_allow_html=True
    )
    uploaded = st.file_uploader(
        "add photo or video",
        type=["jpg", "jpeg", "png", "gif", "mp4", "mov"],
        key=key,
        label_visibility="collapsed",
    )
    if uploaded:
        if uploaded.type.startswith("image"):
            st.image(uploaded, use_container_width=True)
        elif uploaded.type.startswith("video"):
            st.video(uploaded)
        st.markdown(
            f"<div class='memory-caption'>{title.lower()}</div>",
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            "<div class='memory-placeholder'>drop a photo or video here</div>",
            unsafe_allow_html=True
        )
    spacer(12)


# PAGE 1 - WELCOME
if page == "Welcome":
    st.markdown("""
    <div class='page-wrapper' style='text-align:center; padding: 2.5rem 0 1rem 0;'>
        <div class='hero-title'>For Annie</div>
        <div class='hero-subtitle'>a small project, started around valentine's day</div>
    </div>
    """, unsafe_allow_html=True)

    spacer(10)
    st.markdown("<hr class='soft-divider'>", unsafe_allow_html=True)
    spacer(10)

    body(
        "So, not going to lie, this is a bit of a different one. But bear with me.<br><br>"
        "I started building this around Valentine's Day. The plan was to send it on our three months "
        "alongside a letter, just as a way of saying here's what this time actually was. Not a card, "
        "not just a text, something a bit more personal than that. "
        "The idea was to keep adding to it over time as well, like a proper scrapbook but digital.<br><br>"
        "Things changed though, as they do. We stopped speaking as much and the timing I had in my "
        "head didn't really come together. But I kept finishing it anyway because it didn't feel right "
        "just leaving it half done. The moments still happened, they still mattered, "
        "so the project still made sense to exist."
    )

    quote("We didn't work out in the end but ayy, the time was real and that's worth something.")

    body(
        "So if you're reading this, hi. Hope it makes you smile at least a little bit.<br><br>"
        "Use the sidebar to go through it."
    )

    spacer(10)
    st.markdown("""
    <div style='text-align:center; margin-top:1.5rem;'>
        <span class='pill'>three months</span>
        <span class='pill'>valentine's day</span>
        <span class='pill'>made with care</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='footer'>use the sidebar to explore</div>", unsafe_allow_html=True)


# PAGE 2 - APPRECIATION
elif page == "Appreciation":
    page_header("from me to you", "For You, Annie")

    body(
        "Not going to make this weird, I just genuinely think you deserve to hear "
        "some things said properly.<br><br>"
        "You're one of those people that's actually just kind. Not in a fake way, not because "
        "you're trying to be, just kind by default. That's rarer than people realise. "
        "Most people are nice when it's convenient. You're just actually a good person "
        "and it shows without you even trying to make it show."
    )

    quote("You have a way of making people feel like what they're saying actually matters.")

    body(
        "You're thoughtful in a way that runs a bit deeper than most. You think before you speak, "
        "you care about the people around you, and you've got this quiet kind of intelligence that "
        "comes out in the smallest things. A well-timed observation, a genuine question, a moment "
        "where you clearly understood something without needing it explained twice.<br><br>"
        "Getting to know you these past months was genuinely one of the good things. "
        "Not something I'll look back on with any regret, more something I'll remember "
        "with warmth, because that's exactly what it was."
    )

    spacer(8)
    st.markdown("<hr class='soft-divider'>", unsafe_allow_html=True)

    body(
        "I'm grateful for the conversations we had. The ones that started about nothing "
        "and ended somewhere real. The moments where we were just laughing at the exact same "
        "thing at the exact same time. Those don't happen with just anyone.<br><br>"
        "You represent something I think people undervalue. Someone who shows up fully, "
        "who takes things seriously without being heavy about it, "
        "who has enough self-awareness to be both fun and actually meaningful in the same breath. "
        "Meeting you reminded me that people can still surprise you. "
        "That you can be going about your normal life and then someone just quietly shifts "
        "your perspective a bit, just by being themselves."
    )

    quote("Some people just stay with you. Not because of anything dramatic, just because of who they are.")

    body(
        "I think sometimes you don't fully clock what you actually bring to the people around you. "
        "You just get on with things without realising the effect you have. "
        "So just in case no one's said it clearly enough recently, you're appreciated. Genuinely.<br><br>"
        "Thank you for being you, Annie. That's really all this is saying."
    )

    st.markdown("<div class='footer'>x</div>", unsafe_allow_html=True)


# PAGE 3 - MEMORIES
elif page == "Memories":
    page_header("us, documented", "The Memories")

    body(
        "From pretty early on I started holding onto things. Not in a weird way, "
        "just, I knew this was worth remembering. So here's some of it.<br><br>"
        "Add what you want, leave what you want. It's yours as much as it is mine."
    )

    spacer(16)

    memory_slot(
        "night_we_met",
        "The Night We Met",
        "The beginning of all of it. Before anything was figured out or labelled. Just two people in the same place at the same time and something clicking."
    )

    memory_slot(
        "first_date",
        "First Date",
        "When it started feeling like actually something. That shift where you stop just talking and start properly wanting to see where it goes."
    )

    memory_slot(
        "first_sleepover",
        "First Sleepover",
        "When things got comfortable. Not trying to impress anyone, not overthinking anything, just easy."
    )

    memory_slot(
        "funny_moments",
        "Funny Moments",
        "The stupid stuff. The things that probably wouldn't make sense to anyone else but had us gone. Those are honestly the ones I think about most."
    )

    memory_slot(
        "random_moments",
        "Random Ones",
        "The unplanned stuff. Nothing special on paper but somehow ended up being everything."
    )

    memory_slot(
        "quiet_moments",
        "Quiet Moments",
        "When nothing much was happening and it was still exactly where you wanted to be. Those hit different looking back."
    )

    memory_slot(
        "recent",
        "More Recent Ones",
        "The later ones. A bit more bittersweet maybe, but still worth keeping."
    )

    st.markdown("<div class='footer'>x</div>", unsafe_allow_html=True)


# PAGE 4 - SMALL MOMENTS
elif page == "Small Moments":
    page_header("the ones you almost forget", "Small Moments")
    body(
        "Not going to lie, the big moments are easy to hold onto. "
        "It's the small ones that kind of sneak up on you later.<br><br>"
        "The ones that didn't feel like much at the time but somehow end up being "
        "the ones you actually think about."
    )
    quote("The quiet ones always end up being the ones that stick though. You feel me?")
    spacer(6)
    moments = [
        ("walk", "Late walks", "The kind where neither of you really wants to call it yet so you just keep going. Conversation or no conversation, it didn't really matter either way."),
        ("food", "Random food runs", "Nothing planned, nothing fancy. Just hungry and together and that being enough. Some of the best conversations honestly happen in those moments."),
        ("jokes", "The jokes that stuck", "The ones that got funnier every time one of you brought it back up. Inside jokes are basically proof that you were actually paying attention to each other."),
        ("texts", "The texts that landed", "When you're just going about your day and a message comes through and it just makes it better. Small thing but real."),
        ("space", "Just being in the same space", "Not every moment needs to be an event. Sometimes being around someone comfortable is genuinely the whole thing."),
        ("nowords", "The moments that didn't need words", "When something just gets understood without anyone having to say it out loud. That doesn't happen with just anyone."),
    ]
    for key, title, desc in moments:
        st.markdown(
            f"<div class='moment-bubble'>"
            f"<strong style='font-family:\"Cormorant Garamond\",serif; font-size:1.05rem;'>{title}</strong><br>"
            f"{desc}"
            f"</div>",
            unsafe_allow_html=True
        )
        uploaded = st.file_uploader(
            "add a photo or video",
            type=["jpg", "jpeg", "png", "gif", "mp4", "mov"],
            key=f"moment_{key}",
            label_visibility="collapsed",
        )
        if uploaded:
            if uploaded.type.startswith("image"):
                st.image(uploaded, use_container_width=True)
            elif uploaded.type.startswith("video"):
                st.video(uploaded)
            st.markdown(f"<div class='memory-caption'>{title.lower()}</div>", unsafe_allow_html=True)
        else:
            st.markdown("<div class='memory-placeholder'>drop a photo or video here</div>", unsafe_allow_html=True)
        spacer(10)
    st.markdown("<hr class='soft-divider'>", unsafe_allow_html=True)
    body(
        "These are the things I think about when I think about this time. "
        "Not the big stuff, just like the texture of it if that makes sense. The everyday things that you only "
        "properly appreciate once they're a bit further away.<br><br>"
        "Grateful for all of it, even the small bits."
    )
    st.markdown("<div class='footer'>x</div>", unsafe_allow_html=True)

# PAGE 5 - WHY THIS EXISTS
elif page == "Why This Exists":
    page_header("just to be clear", "Why This Exists")

    body(
        "Okay so I want to be straight about this because I don't want it "
        "to come across the wrong way.<br><br>"
        "This wasn't made to put pressure on anything or make anyone feel like "
        "they owe something back. That was genuinely never the point."
    )

    quote("It was just a creative idea for a milestone. That's it.")

    body(
        "The original idea was simple. Since I knew i wasn't gonna ask you out, "
        "I wanted to actually mark three months of getting to know each other properly. "
        "Because that's something. Three months of real conversations, real time, real moments. "
        "That deserved a bit more than just a message.<br><br>"
        "Also not going to lie, it felt unique. I hadn't seen anyone do a digital scrapbook before. "
        "I was going to do a magazine at first but saw it on a TikTok so that lost all the appeal. "
        "And three months felt like a milestone worth doing something for."
    )

    spacer(6)
    st.markdown("<hr class='soft-divider'>", unsafe_allow_html=True)

    body(
        "Our timing didn't really cooperate though. Things changed. "
        "So this sat half done for a bit until I decided to just finish it anyway. "
        "Not for any particular outcome, just because the work was already there "
        "and the intention behind it was still good.<br><br>"
        "Because making something for someone you care about is still worth doing "
        "even if the moment you imagined sharing it has already passed.<br><br>"
        "That's it really. Just appreciation. Nothing more complicated than that."
    )

    quote("No pressure, no expectations. Just something made with care.")

    spacer(6)
    st.markdown("""
    <div style='text-align:center; margin-top:1.5rem;'>
        <span class='pill'>no pressure</span>
        <span class='pill'>no expectations</span>
        <span class='pill'>just appreciation</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='footer'>x</div>", unsafe_allow_html=True)


# PAGE 6 - ACCESS
elif page == "Access":
    page_header("use it anywhere", "Adding It to Your Phone")

    body(
        "I know you not the best with tech stuff, so I wanted to make it as easy as possible for you to access and keep adding to if you want to. :) "
        "You can open this from any device, phone, laptop, tablet, whatever. "
        "No app to download, no account needed, just the link. "
        "And if you want it to sit on your home screen like a proper app, here's how."
    )


    spacer(20)

    st.markdown("""
    <div style='font-family:"Cormorant Garamond",serif; font-size:1.25rem;
         color:#4a2e22; margin-bottom:0.9rem; letter-spacing:0.03em;'>
        Android (Chrome)
    </div>
    """, unsafe_allow_html=True)

    for num, text in [
        ("1", "Open the site in Chrome."),
        ("2", "Tap the three dots in the top right corner."),
        ("3", "Tap <strong>Add to Home screen.</strong>"),
        ("4", "Name it whatever you like."),
        ("5", "Tap Add and it shows up on your home screen like a normal app icon."),
    ]:
        st.markdown(
            f"<div class='step-card'>"
            f"<div class='step-number'>{num}</div>"
            f"<div class='step-text'>{text}</div>"
            f"</div>",
            unsafe_allow_html=True
        )

    spacer(20)
    st.markdown("<hr class='soft-divider'>", unsafe_allow_html=True)

    body(
        "Once it's on your home screen it opens full screen, no browser bar, "
        "just the scrapbook. It'll be there whenever you want to come back to it."
    )

    st.markdown("""
    <div style='text-align:center; margin-top:2rem;'>
        <span class='pill'>works on Android</span>
        <span class='pill'>works everywhere</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='footer'>made with the most amount of care, for you</div>", unsafe_allow_html=True)
