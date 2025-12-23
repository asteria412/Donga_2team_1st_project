import streamlit as st
import base64
import os
import streamlit.components.v1 as components

# 1. 페이지 설정
st.set_page_config(layout="wide", page_title="Mobile Pilot Team Prism")

# ==========================================
# ▼▼▼ [NEW] 프리즘 디자인: 타이틀 추가 ▼▼▼
# ==========================================
st.markdown("""
    <style>
    /* 무지개색 그라데이션 타이틀 스타일 */
    .prism-title {
        font-size: 3em;
        font-weight: 900;
        text-align: center;
        margin-bottom: 10px;
        background: linear-gradient(to right, #ff6b6b, #feca57, #48dbfb, #ff9ff3);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0px 0px 10px rgba(255,255,255,0.3);
        font-family: -apple-system, BlinkMacSystemFont, sans-serif;
    }
    .prism-subtitle {
        text-align: center;
        color: gray;
        font-size: 1.2em;
        margin-top: -10px;
        margin-bottom: 30px;
        font-family: -apple-system, BlinkMacSystemFont, sans-serif;
    }
    </style>
    <h1 class='prism-title'>What's in the creator's mobile?</h1>
    <p class='prism-subtitle'>여섯 개의 색이 모여 만든 하나의 빛 🌈</p>
    """, unsafe_allow_html=True)
# ==========================================


# 2. 이미지 변환 함수
def get_img_as_base64(file_path):
    if not os.path.exists(file_path):
        return ""
    try:
        with open(file_path, "rb") as f:
            data = f.read()
        return f"data:image/png;base64," + base64.b64encode(data).decode()
    except:
        return ""

# 3. 아이콘 로드
icons = {
    "voca": get_img_as_base64("icon_voca.png"),
    "choby": get_img_as_base64("choby_no_bg.png"),
    "shorts": get_img_as_base64("short_maker_no_bg.png"),
    "avatar": get_img_as_base64("아바타_챗봇_no_bg.png"),
    "sorigeul": get_img_as_base64("소리글_no_bg.png"),
    "dual": get_img_as_base64("dual soul_no_bg.png")
}

def check_icon(key, label):
    if icons[key]: return icons[key]
    return f"https://via.placeholder.com/120/a1c4fd/ffffff?text={label}"

# 4. HTML/CSS
mobile_html = f"""
<!DOCTYPE html>
<html>
<head>
<style>
    /* body 높이를 조절하여 타이틀과 간격을 맞춤 */
    body {{ margin: 0; display: flex; justify-content: center; align-items: center; min-height: 75vh; background-color: transparent; font-family: -apple-system, BlinkMacSystemFont, sans-serif; }}
    
    .phone-frame {{ 
        width: 360px; height: 720px; background-color: #111; border-radius: 50px; 
        padding: 15px; position: relative; box-sizing: border-box;
        
        /* ▼▼▼ [수정됨] 평상시에는 빛이 없고 기본 그림자만 있음 ▼▼▼ */
        box-shadow: 0 30px 60px rgba(0,0,0,0.5);
        /* 빛이 확 퍼지는 느낌을 위해 ease-out 사용 */
        transition: box-shadow 0.4s ease-out;
    }}
    
    /* ▼▼▼ [수정됨] 마우스를 올리면 숨겨둔 프리즘 빛이 폭발하듯 퍼져나감 ▼▼▼ */
    .phone-frame:hover {{
         box-shadow: 
            0 40px 80px rgba(0,0,0,0.6), /* 기본 그림자 진하게 */
            0 0 200px rgba(255, 100, 100, 0.5), /* 빨간 빛 폭발 */
            -80px -50px 250px rgba(100, 255, 100, 0.5), /* 초록 빛 폭발 */
            80px -50px 250px rgba(100, 100, 255, 0.5); /* 파란 빛 폭발 */
    }}

    .notch {{ position: absolute; top: 0; left: 50%; transform: translateX(-50%); width: 150px; height: 28px; background-color: #111; border-bottom-left-radius: 16px; border-bottom-right-radius: 16px; z-index: 100; }}
    .screen {{ width: 100%; height: 100%; background: linear-gradient(160deg, #a1c4fd 0%, #c2e9fb 100%); border-radius: 38px; position: relative; overflow: hidden; }}
    input[type="checkbox"] {{ display: none; }}
    
    .folder {{
        position: absolute; top: 120px; left: 25px; width: 70px; height: 70px;
        background-color: rgba(255, 255, 255, 0.35); border-radius: 18px;
        backdrop-filter: blur(8px); display: flex; flex-wrap: wrap;
        justify-content: center; align-items: center; padding: 10px; cursor: pointer;
    }}
    .mini-icon {{ width: 13px; height: 13px; border-radius: 3px; margin: 2px; }}
    
    .folder-label {{ position: absolute; top: 220px; left: 12px; width: 120px; text-align: center; color: white; font-size: 13px; font-weight: bold; text-shadow: 0 1px 3px rgba(0,0,0,0.4); }}
    
    #folder-toggle:checked ~ .folder {{
        top: 50%; left: 50%; width: 300px; height: 380px;
        transform: translate(-50%, -50%); background-color: rgba(255, 255, 255, 0.9);
        border-radius: 30px; padding: 25px 20px; z-index: 200; cursor: default;
    }}
    #folder-toggle:checked ~ .folder .mini-icon, #folder-toggle:checked ~ .folder-label {{ display: none; }}

    /* ▼▼▼ 여기 숫자를 고치면 위치가 변해요! ▼▼▼ */
    .app-grid {{
        display: none; width: 100%; height: 100%; flex-wrap: wrap;
        align-content: flex-start; gap: 10px;
        padding-left: 12px; /* 아까 24px -> 12px로 줄였습니다 (더 왼쪽으로 옴) */
    }}
    #folder-toggle:checked ~ .folder .app-grid {{ display: flex; }}
    
    .folder-title {{ 
        width: 100%; font-size: 20px; font-weight: bold; 
        margin-bottom: 20px; text-align: center; color: #333; 
        margin-left: -12px; /* 제목 중앙 정렬을 위해 padding만큼 반대로 당김 */
    }}
    
    .app-item {{ display: flex; flex-direction: column; align-items: center; width: 80px; margin-bottom: 10px; text-decoration: none; transition: transform 0.2s; }}
    .app-item:hover {{ transform: scale(1.1); }} /* 마우스 호버 시 아이콘 확대 효과 추가 */
    .app-img {{ width: 60px; height: 60px; border-radius: 12px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); object-fit: cover; }}
    .app-name {{ margin-top: 6px; font-size: 11px; color: #333; font-weight: 600; text-align: center; }}
</style>
</head>
<body>
    <div class="phone-frame">
        <div class="notch"></div>
        <div class="screen">
            <input type="checkbox" id="folder-toggle">
            <label for="folder-toggle" class="folder">
                <div class="mini-icon" style="background-color: #ffb7b2;"></div> <div class="mini-icon" style="background-color: #b5ead7;"></div> <div class="mini-icon" style="background-color: #a0c4ff;"></div> <div class="mini-icon" style="background-color: #e2bbfd;"></div> 
                
                <div class="app-grid">
                    <div class="folder-title">My favorite</div>
                    
                    <a href="https://llm-proj-202512-88cccgb64yuvuu97z3ugwu.streamlit.app/" target="_blank" class="app-item">
                        <img src="{check_icon('shorts', 'Shorts')}" class="app-img">
                        <div class="app-name">Shorts Maker</div>
                    </a>

                    <a href="https://donga2teamproject1-choby.streamlit.app/" target="_blank" class="app-item">
                        <img src="{check_icon('choby', 'Choby')}" class="app-img">
                        <div class="app-name">CHOBY(SNS)</div>
                    </a>

                    <a href="https://llm-1stproject-rzz5dv7tojel4tjhercgep.streamlit.app/ " target="_blank" class="app-item">
                        <img src="{check_icon('sorigeul', 'Record')}" class="app-img">
                        <div class="app-name">소리글</div>
                    </a>

                    <a href="https://cnvocahigh.streamlit.app" target="_blank" class="app-item">
                        <img src="{check_icon('voca', 'Voca')}" class="app-img">
                        <div class="app-name">voca海</div>
                    </a>

                    <a href="여기에_아바타_링크를_넣으세요" target="_blank" class="app-item">
                        <img src="{check_icon('avatar', 'Avatar')}" class="app-img">
                        <div class="app-name">아바타 챗봇</div>
                    </a>

                    <a href="https://dualsoul.streamlit.app/" target="_blank" class="app-item">
                        <img src="{check_icon('dual', 'Tarot')}" class="app-img">
                        <div class="app-name">Dual Soul</div>
                    </a>

                </div>
            </label>
            <div class="folder-label">My favorite</div>
        </div>
    </div>
</body>
</html>
"""

# 타이틀 공간 확보를 위해 높이를 조금 늘렸습니다
components.html(mobile_html, height=850)