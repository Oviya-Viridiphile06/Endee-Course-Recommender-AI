import streamlit as st
from recommender import Recommender

st.set_page_config(page_title="AI Course Recommender", layout="wide")

st.title("🎓 AI Course Recommendation System")
st.markdown("Smart semantic AI recommender")

rec = Recommender()

# ---------------- FORM ----------------
with st.form(key="search_form"):
    query = st.text_input("Enter your interest (e.g. machine learning, cloud, python)")
    submitted = st.form_submit_button("🚀 Recommend")

# ---------------- ONLY RUN AFTER CLICK ----------------
if submitted:

    if not query or not query.strip():
        st.warning("Please enter a valid interest.")

    else:
        results = rec.recommend(query)[:8]   # ✅ FIXED HERE

        st.markdown("## 📚 Recommended Courses")

        for i in range(0, len(results), 3):

            cols = st.columns(3, gap="large")

            for j in range(3):

                if i + j < len(results):
                    r = results[i + j]
                    rank = i + j + 1

                    with cols[j]:

                        st.markdown(f"""
                        <div style="
                            border:1px solid #1f2937;
                            border-radius:16px;
                            padding:18px;
                            margin-bottom:16px;
                            background:#0f172a;
                            box-shadow:0 4px 14px rgba(0,0,0,0.3);
                            min-height:340px;
                        ">

                        <h3 style="
                            color:#f8fafc;
                            margin-bottom:10px;
                            font-size:18px;
                            font-weight:700;
                            line-height:1.3;
                        ">
                        {rank}. {r['title']}
                        </h3>

                        <p style="
                            color:#cbd5e1;
                            font-size:14px;
                            line-height:1.5;
                            margin-bottom:12px;
                        ">
                        {r['description']}
                        </p>

                        <hr style="border:0.5px solid #334155;">

                        <p style="
                            color:#94a3b8;
                            font-size:13.5px;
                            line-height:1.6;
                        ">
                        🎯 <b>Level:</b> {r['level']}<br>
                        ⭐ <b>Rating:</b> {r['rating']}<br>
                        📊 <b>Score:</b> {r['score']}
                        </p>

                        <div style="
                            margin-top:10px;
                            padding:10px;
                            border-radius:10px;
                            background:#111827;
                        ">

                        <b style="
                            color:#38bdf8;
                            font-size:14px;
                        ">
                        {r['website']['name']}
                        </b><br>

                        <small style="
                            color:#9ca3af;
                            font-size:12.5px;
                            line-height:1.4;
                        ">
                        {r['website']['desc']}
                        </small><br><br>

                        <a href="{r['website']['link']}" target="_blank"
                        style="
                            color:#60a5fa;
                            text-decoration:none;
                            font-weight:700;
                            font-size:13px;
                        ">
                        👉 Visit Course
                        </a>

                        </div>

                        </div>
                        """, unsafe_allow_html=True)