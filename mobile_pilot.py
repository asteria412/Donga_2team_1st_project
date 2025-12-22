import streamlit as st
import base64
import os
import streamlit.components.v1 as components

st.set_page_config(layout="wide", page_title="Mobile Pilot")

def get_img_as_base64(file_path):
    if not os.path.exists(file_path):
        return None
    with open(file_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

voca_icon_b64 = get_img_as_base64("icon_voca.png")
if voca_icon_b64:
    icon_src = f"data:image/png;base64,{voca_icon_b64}"
else:
    icon_src = "https://via.placeholder.com/60?text=Voca"

mobile_html = f"""
<!DOCTYPE html>
<html>
<head>
<style>
    body {{
        margin: 0;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        background-color: #f0f2f6;
        font-family: -apple-system, BlinkMacSystemFont, sans-serif;
    }}
    .phone-frame {{
        width: 360px;
        height: 720px;
        background-color: #111;
        border-radius: 50px;
        box-shadow: 0 30px 60px rgba(0,0,0,0.4);
        padding: 15px;
        position: relative;
        box-sizing: border-box;
    }}
    .notch {{
        position: absolute;
        top: 0;
        left: 50%;
        transform: translateX(-50%);
        width: 150px;
        height: 28px;
        background-color: #111;
        border-bottom-left-radius: 16px;
        border-bottom-right-radius: 16px;
        z-index: 100;
    }}
    .screen {{
        width: 100%;
        height: 100%;
        background: linear-gradient(160deg, #a1c4fd 0%, #c2e9fb 100%);
        border-radius: 38px;
        position: relative;
        overflow: hidden;
        animation: turnOn 1.2s ease-out forwards;
    }}
    @keyframes turnOn {{
        0% {{ filter: brightness(0); opacity: 0; }}
        40% {{ filter: brightness(0.1); opacity: 1; }}
        100% {{ filter: brightness(1); opacity: 1; }}
    }}
    .status-bar {{
        padding: 14px 22px;
        display: flex;
        justify-content: space-between;
        color: white;
        font-size: 13px;
        font-weight: 600;
    }}
    input[type="checkbox"] {{ display: none; }}
    .folder {{
        position: absolute;
        top: 120px;
        left: 25px;
        width: 70px;
        height: 70px;
        background-color: rgba(255, 255, 255, 0.35);
        border-radius: 18px;
        backdrop-filter: blur(8px);
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        align-items: center;
        padding: 10px;
        cursor: pointer;
        transition: all 0.4s cubic-bezier(0.25, 1, 0.5, 1);
        z-index: 10;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
    }}
    .mini-icon {{
        width: 13px;
        height: 13px;
        background-color: white;
        border-radius: 3px;
        margin: 2px;
        opacity: 0.9;
    }}
    .folder-label {{
    position: absolute;
    top: 220px;
    left: 12px;
    width: 120px;
    white-space: nowrap;
    text-align: center;
    color: white;
    font-size: 13px;
    text-shadow: 0 1px 3px rgba(0,0,0,0.4);
    font-weight: bold;
    }}
    
    #folder-toggle:checked ~ .folder {{
        top: 50%;
        left: 50%;
        width: 300px;
        height: 320px;
        transform: translate(-50%, -50%);
        background-color: rgba(255, 255, 255, 0.9);
        border-radius: 30px;
        cursor: default;
        padding: 20px;
        box-shadow: 0 20px 50px rgba(0,0,0,0.2);
    }}
    #folder-toggle:checked ~ .folder .mini-icon {{ display: none; }}
    #folder-toggle:checked ~ .folder-label {{ opacity: 0; }}
    .app-grid {{
        display: none;
        width: 100%;
        height: 100%;
        flex-wrap: wrap;
        align-content: flex-start;
        gap: 15px;
    }}
    #folder-toggle:checked ~ .folder .app-grid {{
        display: flex;
        animation: fadeIn 0.4s ease 0.2s forwards;
        opacity: 0;
    }}
    @keyframes fadeIn {{ 
        from {{ opacity: 0; transform: translateY(10px); }} 
        to {{ opacity: 1; transform: translateY(0); }} 
    }}
    .folder-title {{
        width: 100%;
        font-size: 20px;
        font-weight: bold;
        color: #333;
        margin-bottom: 20px;
        text-align: center;
    }}
    .app-item {{
        display: flex;
        flex-direction: column;
        align-items: center;
        text-decoration: none !important;
        width: 75px;
        margin-bottom: 10px;
        transition: transform 0.1s;
        cursor: pointer;
    }}
    .app-item:hover {{ transform: scale(1.05); }}
    .app-img {{
        width: 60px;
        height: 60px;
        border-radius: 12px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.15);
        object-fit: cover;
    }}
    .app-name {{
        margin-top: 6px;
        font-size: 12px;
        color: #333;
        font-weight: 600;
        text-align: center;
    }}
</style>
</head>
<body>
    <div class="phone-frame">
        <div class="notch"></div>
        <div class="screen">
            <div class="status-bar">
                <span>12:00</span>
                <span>5G 100%</span>
            </div>
            <input type="checkbox" id="folder-toggle">
            <label for="folder-toggle" class="folder">
                <div class="mini-icon" style="background-color: #3498db;"></div> 
                <div class="mini-icon"></div>
                <div class="mini-icon"></div>
                <div class="mini-icon"></div>
                <div class="app-grid">
                    <div class="folder-title">My favorite</div>
                    <a href="https://cnvocahigh.streamlit.app" target="_blank" class="app-item">
                        <img src="{icon_src}" class="app-img">
                        <div class="app-name">voca海</div>
                    </a>
                </div>
            </label>
            <div class="folder-label">My favorite</div>
        </div>
    </div>
</body>
</html>
"""

components.html(mobile_html, height=800, scrolling=False)