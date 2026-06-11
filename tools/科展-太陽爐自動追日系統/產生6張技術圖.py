#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
產生 6 張太陽爐雙軸追日系統技術圖
使用 matplotlib 繪製工程線稿圖
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np
import os

# 設定中文字型
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei', '微軟正黑體', 'SimHei']
plt.rcParams['axes.unicode_minus'] = False

OUT = r'G:\我的雲端硬碟\solar-furnace\tools\科展-太陽爐自動追日系統\技術圖'
os.makedirs(OUT, exist_ok=True)

# ============================================================
# 001 整體3D結構圖
# ============================================================
def draw_001():
    fig, ax = plt.subplots(1, 1, figsize=(16, 12))
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 12)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_facecolor('#FFFEF5')
    fig.patch.set_facecolor('#FFFEF5')

    # 標題
    ax.text(8, 11.3, '太陽爐雙軸追日系統 — 整體結構圖', fontsize=18, fontweight='bold',
            ha='center', va='center', color='#1a5276')

    # --- 底座 ---
    base = FancyBboxPatch((3, 1.5), 6, 0.6, boxstyle="round,pad=0.05",
                          facecolor='#DEB887', edgecolor='#8B4513', linewidth=2)
    ax.add_patch(base)
    ax.text(6, 1.8, '① 底座 30×30cm 木板', fontsize=9, ha='center', color='#8B4513', fontweight='bold')

    # 止滑墊
    for x in [3.3, 8.7]:
        pad = FancyBboxPatch((x-0.15, 1.35), 0.3, 0.15, boxstyle="round,pad=0.02",
                             facecolor='#555', edgecolor='#333', linewidth=1)
        ax.add_patch(pad)
    ax.text(6, 1.15, '止滑墊 ×4', fontsize=7, ha='center', color='#555')

    # --- 中心軸 ---
    ax.plot([6, 6], [2.1, 5.5], color='#708090', linewidth=4, solid_capstyle='round')
    ax.plot([6], [2.1], marker='^', markersize=8, color='#708090')
    ax.text(6.3, 3.8, '② M8 中心軸\n   (15cm)', fontsize=8, color='#708090', fontweight='bold')

    # --- 轉盤 ---
    turntable = FancyBboxPatch((3.5, 3.0), 5, 0.4, boxstyle="round,pad=0.05",
                               facecolor='#F5DEB3', edgecolor='#8B4513', linewidth=2)
    ax.add_patch(turntable)
    ax.text(6, 3.2, '③ 轉盤 25×25cm', fontsize=9, ha='center', color='#8B4513', fontweight='bold')

    # 軸承 (4顆)
    for dx, dy in [(-1.2, 0.2), (1.2, 0.2), (-1.2, -0.2), (1.2, -0.2)]:
        bearing = plt.Circle((6+dx, 3.2+dy), 0.12, facecolor='#C0C0C0', edgecolor='#808080', linewidth=1.5)
        ax.add_patch(bearing)
    ax.text(6, 2.7, '608ZZ ×4', fontsize=7, ha='center', color='#808080')

    # --- 立柱 ---
    for x in [4.0, 8.0]:
        col = FancyBboxPatch((x-0.12, 3.4), 0.24, 2.5, boxstyle="round,pad=0.02",
                             facecolor='#DEB887', edgecolor='#8B4513', linewidth=1.5)
        ax.add_patch(col)
    ax.text(3.3, 4.6, '④ 立柱\n   2×2×20cm\n   ×2', fontsize=8, color='#8B4513', fontweight='bold')

    # 立柱頂端孔
    for x in [4.0, 8.0]:
        hole = plt.Circle((x, 5.85), 0.08, facecolor='white', edgecolor='#8B4513', linewidth=1)
        ax.add_patch(hole)

    # --- 太陽爐（拋物面）---
    theta = np.linspace(-0.8, 0.8, 50)
    x_furnace = 6 + 1.8 * np.sin(theta)
    y_furnace = 5.5 + 1.5 * np.cos(theta) * 0.6
    ax.plot(x_furnace, y_furnace, color='#4FC3F7', linewidth=3)
    ax.fill_between(x_furnace, y_furnace, y_furnace-0.15, color='#B3E5FC', alpha=0.7)
    # 鏡面反光線
    for i in range(7):
        xi = 4.8 + i * 0.35
        ax.plot([xi, 6], [y_furnace[i*7] if i*7 < len(y_furnace) else 6.2, 6.5],
                color='#87CEEB', linewidth=0.8, alpha=0.5)
    ax.text(6, 7.0, '⑤ 太陽爐 (18片拋物面鏡)', fontsize=9, ha='center',
            color='#0277BD', fontweight='bold')

    # 焦點
    ax.plot(6, 6.5, marker='*', markersize=15, color='#FF4500')
    ax.text(6.4, 6.5, '焦點\n10cm', fontsize=7, color='#FF4500')

    # --- 水平馬達 ---
    motor_h = FancyBboxPatch((3.2, 2.0), 0.8, 0.5, boxstyle="round,pad=0.05",
                             facecolor='#90A4AE', edgecolor='#455A64', linewidth=1.5)
    ax.add_patch(motor_h)
    ax.text(3.6, 2.25, '⑥', fontsize=10, ha='center', color='white', fontweight='bold')
    ax.text(2.5, 2.25, '水平\nMG996R', fontsize=8, ha='center', color='#455A64', fontweight='bold')

    # 小齒輪
    gear_s = plt.Circle((4.1, 2.55), 0.12, facecolor='#FFB74D', edgecolor='#E65100', linewidth=1)
    ax.add_patch(gear_s)
    ax.text(4.1, 2.55, '10T', fontsize=5, ha='center', va='center', color='#E65100')

    # 大齒輪
    gear_l = plt.Circle((6, 3.0), 0.5, facecolor='#FFCC80', edgecolor='#E65100',
                         linewidth=1.5, linestyle='--')
    ax.add_patch(gear_l)
    ax.text(6, 3.0, '60T', fontsize=6, ha='center', va='center', color='#E65100')

    # --- 垂直馬達 ---
    motor_v = FancyBboxPatch((8.3, 4.0), 0.5, 0.8, boxstyle="round,pad=0.05",
                             facecolor='#90A4AE', edgecolor='#455A64', linewidth=1.5)
    ax.add_patch(motor_v)
    ax.text(8.55, 4.4, '⑦', fontsize=10, ha='center', color='white', fontweight='bold')
    ax.text(9.3, 4.4, '垂直\nMG996R', fontsize=8, ha='center', color='#455A64', fontweight='bold')

    # 連桿
    ax.plot([8.3, 7.8], [4.8, 5.5], color='#455A64', linewidth=2)
    ax.text(8.5, 5.1, '連桿', fontsize=7, color='#455A64')

    # --- 配重 ---
    ax.plot([7.8, 7.8], [5.5, 4.5], color='#795548', linewidth=1.5, linestyle='--')
    weight = FancyBboxPatch((7.55, 4.0), 0.5, 0.5, boxstyle="round,pad=0.05",
                            facecolor='#795548', edgecolor='#4E342E', linewidth=1.5)
    ax.add_patch(weight)
    ax.text(7.8, 4.25, '⑧', fontsize=9, ha='center', color='white', fontweight='bold')
    ax.text(7.8, 3.6, '配重 ~300g', fontsize=7, ha='center', color='#4E342E', fontweight='bold')

    # --- LDR 標示 ---
    for dx, dy, label in [(-1.5, 0.8, 'LDR左'), (1.5, 0.8, 'LDR右'),
                          (0, 1.3, 'LDR上'), (0, 0.3, 'LDR下')]:
        ldr = plt.Circle((6+dx, 5.8+dy), 0.08, facecolor='#FFEB3B', edgecolor='#F57F17', linewidth=1)
        ax.add_patch(ldr)
    ax.text(6, 7.5, 'LDR ×4', fontsize=7, ha='center', color='#F57F17')

    # --- 角度標示 ---
    ax.annotate('', xy=(8.5, 6.5), xytext=(8.5, 5.5),
                arrowprops=dict(arrowstyle='<->', color='#E53935', lw=1.5))
    ax.text(9.0, 6.0, '0°~80°', fontsize=8, color='#E53935', fontweight='bold')

    # --- 圖例 ---
    legend_items = [
        ('底座/轉盤/立柱', '#DEB887'),
        ('中心軸/螺桿', '#708090'),
        ('伺服馬達', '#90A4AE'),
        ('齒輪', '#FFB74D'),
        ('太陽爐', '#4FC3F7'),
        ('配重', '#795548'),
        ('LDR', '#FFEB3B'),
    ]
    for i, (label, color) in enumerate(legend_items):
        rect = FancyBboxPatch((0.3, 10.5-i*0.35), 0.25, 0.2, boxstyle="round,pad=0.02",
                              facecolor=color, edgecolor='#333', linewidth=0.8)
        ax.add_patch(rect)
        ax.text(0.7, 10.6-i*0.35, label, fontsize=7, va='center', color='#333')

    plt.tight_layout()
    plt.savefig(os.path.join(OUT, '001_整體3D結構圖.png'), dpi=200, bbox_inches='tight',
                facecolor='#FFFEF5')
    plt.close()
    print('001 OK')

# ============================================================
# 002 爆炸圖
# ============================================================
def draw_002():
    fig, ax = plt.subplots(1, 1, figsize=(16, 14))
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 14)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_facecolor('#FFFEF5')
    fig.patch.set_facecolor('#FFFEF5')

    ax.text(8, 13.3, '太陽爐雙軸追日系統 — 爆炸圖（組裝順序）', fontsize=18,
            fontweight='bold', ha='center', color='#1a5276')

    layers = [
        (1.5, '第1層：底座', '30×30cm 木板\n8.5mm 中心孔', '#DEB887', 6, 0.5),
        (3.0, '第2層：中心軸', 'M8 螺桿 15cm\n+ 螺帽固定', '#708090', 6, 1.5),
        (5.0, '第3層：轉盤', '25×25cm 木板\n4× 608ZZ 軸承', '#F5DEB3', 6, 0.5),
        (6.5, '第4層：立柱', '2×2×20cm ×2\n頂端 6mm 孔', '#DEB887', 4.5, 1.5),
        (6.5, '', '', '#DEB887', 7.5, 1.5),
        (8.5, '第5層：轉軸', 'M6 螺桿 10cm ×2', '#708090', 6, 0.3),
        (10.0, '第6層：太陽爐', '18片拋物面鏡\n+ 木塊固定座', '#4FC3F7', 6, 1.2),
        (11.8, '第7層：馬達', 'MG996R ×2\n(水平+垂直)', '#90A4AE', 5, 0.6),
        (11.8, '', '', '#90A4AE', 7, 0.6),
        (12.8, '第8層：齒輪', '60T 大齒輪 + 10T 小齒輪', '#FFB74D', 6, 0.3),
    ]

    for y, title, desc, color, x, h in layers:
        if title == '' and x == 7.5:
            continue
        box = FancyBboxPatch((x-1.5, y), 3, h, boxstyle="round,pad=0.08",
                             facecolor=color, edgecolor='#555', linewidth=1.5, alpha=0.85)
        ax.add_patch(box)
        if title:
            ax.text(x, y+h+0.15, title, fontsize=8, ha='center', fontweight='bold', color='#333')
        if desc:
            ax.text(x, y+h/2, desc, fontsize=7, ha='center', va='center', color='#333')

    # 連接虛線
    for y1, y2 in [(2.0, 3.0), (4.5, 5.0), (5.5, 6.5), (8.0, 8.5), (8.8, 10.0),
                   (11.2, 11.8), (12.4, 12.8)]:
        ax.plot([6, 6], [y1, y2], color='#999', linewidth=0.8, linestyle='--')

    # 箭頭標示組裝方向
    ax.annotate('', xy=(6, 12.8), xytext=(6, 1.5),
                arrowprops=dict(arrowstyle='->', color='#E53935', lw=2, linestyle='--'))
    ax.text(1.5, 7, '組\n裝\n方\n向', fontsize=12, ha='center', color='#E53935',
            fontweight='bold', rotation=0)

    # 右側說明
    notes = [
        '所有零件從下往上組裝',
        '中心軸先固定在底座',
        '轉盤套入中心軸（軸承內圈）',
        '立柱鎖在轉盤上',
        '太陽爐穿過轉軸架在立柱間',
        '馬達固定後連接齒輪',
    ]
    for i, note in enumerate(notes):
        ax.text(12, 12.5-i*0.5, f'{i+1}. {note}', fontsize=8, color='#555')

    plt.tight_layout()
    plt.savefig(os.path.join(OUT, '002_爆炸圖.png'), dpi=200, bbox_inches='tight',
                facecolor='#FFFEF5')
    plt.close()
    print('002 OK')

# ============================================================
# 003 側面結構圖
# ============================================================
def draw_003():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 10))
    for ax in [ax1, ax2]:
        ax.set_aspect('equal')
        ax.axis('off')
        ax.set_facecolor('#FFFEF5')
    fig.patch.set_facecolor('#FFFEF5')

    fig.suptitle('太陽爐雙軸追日系統 — 側面結構圖', fontsize=18, fontweight='bold',
                 color='#1a5276', y=0.97)

    # --- 左圖：側面尺寸標註 ---
    ax = ax1
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_title('側面圖（含尺寸標註）', fontsize=12, fontweight='bold', pad=10)

    # 底座
    base = FancyBboxPatch((1, 1.5), 6, 0.4, boxstyle="round,pad=0.03",
                          facecolor='#DEB887', edgecolor='#8B4513', linewidth=2)
    ax.add_patch(base)

    # 轉盤
    tt = FancyBboxPatch((1.5, 2.2), 5, 0.3, boxstyle="round,pad=0.03",
                        facecolor='#F5DEB3', edgecolor='#8B4513', linewidth=2)
    ax.add_patch(tt)

    # 中心軸
    ax.plot([4, 4], [1.9, 6.5], color='#708090', linewidth=3)

    # 立柱
    for x in [2.2, 5.8]:
        col = FancyBboxPatch((x-0.1, 2.5), 0.2, 3.5, boxstyle="round,pad=0.02",
                             facecolor='#DEB887', edgecolor='#8B4513', linewidth=1.5)
        ax.add_patch(col)

    # 太陽爐（傾斜）
    theta = np.linspace(-0.6, 0.6, 30)
    xf = 4 + 1.5 * np.sin(theta)
    yf = 5.5 + 1.0 * np.cos(theta) * 0.5
    ax.plot(xf, yf, color='#4FC3F7', linewidth=3)
    ax.fill_between(xf, yf, yf-0.1, color='#B3E5FC', alpha=0.6)

    # LDR 位置
    for dx, dy in [(-1.2, 0.5), (1.2, 0.5), (0, 0.9), (0, 0.1)]:
        ldr = plt.Circle((4+dx, 5.8+dy), 0.06, facecolor='#FFEB3B', edgecolor='#F57F17')
        ax.add_patch(ldr)

    # 水平馬達
    m_h = FancyBboxPatch((1.8, 1.7), 0.6, 0.4, boxstyle="round,pad=0.03",
                         facecolor='#90A4AE', edgecolor='#455A64', linewidth=1)
    ax.add_patch(m_h)

    # 垂直馬達
    m_v = FancyBboxPatch((5.9, 4.0), 0.4, 0.6, boxstyle="round,pad=0.03",
                         facecolor='#90A4AE', edgecolor='#455A64', linewidth=1)
    ax.add_patch(m_v)

    # 配重
    ax.plot([5.8, 5.8], [5.5, 4.5], color='#795548', linewidth=1.5, linestyle='--')
    w = FancyBboxPatch((5.6, 4.0), 0.4, 0.5, boxstyle="round,pad=0.03",
                       facecolor='#795548', edgecolor='#4E342E', linewidth=1)
    ax.add_patch(w)

    # 尺寸標線
    def dim_line(ax, x1, y1, x2, y2, text, offset=0.3, color='#E53935'):
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle='<->', color=color, lw=1.2))
        mx, my = (x1+x2)/2, (y1+y2)/2
        ax.text(mx+offset, my, text, fontsize=7, color=color, ha='left', fontweight='bold')

    dim_line(ax, 1, 1.2, 7, 1.2, '30cm', offset=0)
    dim_line(ax, 1.5, 1.9, 6.5, 1.9, '25cm', offset=0)
    dim_line(ax, 0.8, 2.5, 0.8, 6.0, '20cm', offset=-0.4)
    dim_line(ax, 4.2, 1.9, 4.2, 6.5, '15cm', offset=0.3)
    dim_line(ax, 7.2, 5.0, 7.2, 6.2, '10cm 焦距', offset=0.3)

    # 角度標示
    ax.annotate('', xy=(6.5, 7.0), xytext=(5.5, 5.5),
                arrowprops=dict(arrowstyle='<->', color='#E53935', lw=1.5))
    ax.text(6.8, 6.2, '0°~80°', fontsize=8, color='#E53935', fontweight='bold')

    # gap 標示
    ax.annotate('', xy=(7.5, 2.5), xytext=(7.5, 2.2),
                arrowprops=dict(arrowstyle='<->', color='#E53935', lw=1))
    ax.text(7.8, 2.35, '5mm', fontsize=7, color='#E53935')

    # --- 右圖：正面圖 ---
    ax = ax2
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_title('正面圖', fontsize=12, fontweight='bold', pad=10)

    # 底座
    base = FancyBboxPatch((1.5, 1.5), 5, 0.4, boxstyle="round,pad=0.03",
                          facecolor='#DEB887', edgecolor='#8B4513', linewidth=2)
    ax.add_patch(base)

    # 轉盤
    tt = FancyBboxPatch((2, 2.2), 4, 0.3, boxstyle="round,pad=0.03",
                        facecolor='#F5DEB3', edgecolor='#8B4513', linewidth=2)
    ax.add_patch(tt)

    # 立柱
    for x in [2.8, 5.2]:
        col = FancyBboxPatch((x-0.1, 2.5), 0.2, 3.0, boxstyle="round,pad=0.02",
                             facecolor='#DEB887', edgecolor='#8B4513', linewidth=1.5)
        ax.add_patch(col)

    # 太陽爐（正面看是方形）
    furnace = FancyBboxPatch((3.0, 4.5), 2, 1.8, boxstyle="round,pad=0.05",
                             facecolor='#B3E5FC', edgecolor='#4FC3F7', linewidth=2)
    ax.add_patch(furnace)
    ax.text(4, 5.4, '太陽爐\n(正面)', fontsize=8, ha='center', va='center',
            color='#0277BD', fontweight='bold')

    # 水平馬達
    m = FancyBboxPatch((1.8, 1.7), 0.6, 0.4, boxstyle="round,pad=0.03",
                       facecolor='#90A4AE', edgecolor='#455A64', linewidth=1)
    ax.add_patch(m)
    ax.text(2.1, 1.9, '水平', fontsize=6, ha='center', color='white')

    # 垂直馬達
    m2 = FancyBboxPatch((5.5, 3.5), 0.4, 0.5, boxstyle="round,pad=0.03",
                        facecolor='#90A4AE', edgecolor='#455A64', linewidth=1)
    ax.add_patch(m2)
    ax.text(5.7, 3.75, '垂直', fontsize=6, ha='center', color='white')

    plt.tight_layout()
    plt.savefig(os.path.join(OUT, '003_側面結構圖.png'), dpi=200, bbox_inches='tight',
                facecolor='#FFFEF5')
    plt.close()
    print('003 OK')

# ============================================================
# 004 水平轉動盤詳細圖
# ============================================================
def draw_004():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 10))
    for ax in [ax1, ax2]:
        ax.set_aspect('equal')
        ax.axis('off')
        ax.set_facecolor('#FFFEF5')
    fig.patch.set_facecolor('#FFFEF5')

    fig.suptitle('水平轉動盤詳細圖', fontsize=18, fontweight='bold',
                 color='#1a5276', y=0.97)

    # --- 左圖：俯視圖 ---
    ax = ax1
    ax.set_xlim(-4, 4)
    ax.set_ylim(-4, 4)
    ax.set_title('俯視圖 (Top View)', fontsize=12, fontweight='bold', pad=10)

    # 轉盤
    tt = FancyBboxPatch((-2.5, -2.5), 5, 5, boxstyle="round,pad=0.1",
                        facecolor='#F5DEB3', edgecolor='#8B4513', linewidth=2)
    ax.add_patch(tt)

    # 大齒輪（虛線圓）
    gear_l = plt.Circle((0, 0), 2.2, facecolor='none', edgecolor='#E65100',
                         linewidth=1.5, linestyle='--')
    ax.add_patch(gear_l)
    ax.text(0, -2.5, '60T 大齒輪', fontsize=8, ha='center', color='#E65100')

    # 中心孔
    center = plt.Circle((0, 0), 0.15, facecolor='white', edgecolor='#333', linewidth=2)
    ax.add_patch(center)
    ax.text(0.3, 0.3, '中心孔\n8.5mm', fontsize=7, color='#333')

    # 4 顆軸承（十字排列）
    for dx, dy in [(-1.2, 0), (1.2, 0), (0, -1.2), (0, 1.2)]:
        b_outer = plt.Circle((dx, dy), 0.25, facecolor='#C0C0C0', edgecolor='#808080', linewidth=1.5)
        ax.add_patch(b_outer)
        b_inner = plt.Circle((dx, dy), 0.08, facecolor='white', edgecolor='#808080', linewidth=1)
        ax.add_patch(b_inner)
    ax.text(1.8, 1.0, '608ZZ ×4', fontsize=8, color='#808080', fontweight='bold')

    # 止滑墊
    for x, y in [(-2.3, -2.3), (2.1, -2.3), (-2.3, 2.1), (2.1, 2.1)]:
        pad = FancyBboxPatch((x, y), 0.3, 0.3, boxstyle="round,pad=0.02",
                             facecolor='#555', edgecolor='#333', linewidth=0.8)
        ax.add_patch(pad)

    # 尺寸標線
    ax.annotate('', xy=(2.5, -3.2), xytext=(-2.5, -3.2),
                arrowprops=dict(arrowstyle='<->', color='#E53935', lw=1.2))
    ax.text(0, -3.5, '25cm', fontsize=9, ha='center', color='#E53935', fontweight='bold')

    ax.annotate('', xy=(-3.2, 2.5), xytext=(-3.2, -2.5),
                arrowprops=dict(arrowstyle='<->', color='#E53935', lw=1.2))
    ax.text(-3.5, 0, '25cm', fontsize=9, ha='center', color='#E53935', fontweight='bold',
            rotation=90)

    # --- 右圖：剖面圖 A-A ---
    ax = ax2
    ax.set_xlim(-4, 4)
    ax.set_ylim(-1, 8)
    ax.set_title('剖面圖 A-A (Cross-section)', fontsize=12, fontweight='bold', pad=10)

    # 底座
    base = FancyBboxPatch((-2.5, 0), 5, 0.5, boxstyle="round,pad=0.05",
                          facecolor='#DEB887', edgecolor='#8B4513', linewidth=2)
    ax.add_patch(base)
    ax.text(0, 0.25, '底座 30cm', fontsize=8, ha='center', va='center', color='#8B4513')

    # 中心軸
    ax.plot([0, 0], [0.5, 5.5], color='#708090', linewidth=4)
    ax.text(0.3, 3.0, 'M8\n中心軸', fontsize=7, color='#708090')

    # 軸承（剖面）
    for y in [1.2, 1.8]:
        rect = FancyBboxPatch((-0.35, y), 0.7, 0.25, boxstyle="round,pad=0.02",
                              facecolor='#C0C0C0', edgecolor='#808080', linewidth=1)
        ax.add_patch(rect)
    ax.text(-1.5, 1.5, '608ZZ\n軸承', fontsize=7, color='#808080', ha='center')

    # 轉盤
    tt = FancyBboxPatch((-2, 2.2), 4, 0.3, boxstyle="round,pad=0.03",
                        facecolor='#F5DEB3', edgecolor='#8B4513', linewidth=2)
    ax.add_patch(tt)
    ax.text(0, 2.35, '轉盤 25cm', fontsize=8, ha='center', va='center', color='#8B4513')

    # 7mm 間隙
    ax.annotate('', xy=(2.8, 2.2), xytext=(2.8, 1.8),
                arrowprops=dict(arrowstyle='<->', color='#E53935', lw=1))
    ax.text(3.1, 2.0, '7mm', fontsize=7, color='#E53935')

    # 大齒輪（轉盤底部）
    gear = FancyBboxPatch((-1.5, 1.9), 3, 0.3, boxstyle="round,pad=0.02",
                          facecolor='#FFCC80', edgecolor='#E65100', linewidth=1.5)
    ax.add_patch(gear)
    ax.text(0, 2.05, '60T 大齒輪', fontsize=7, ha='center', va='center', color='#E65100')

    # 小齒輪
    gear_s = plt.Circle((2.2, 1.8), 0.2, facecolor='#FFB74D', edgecolor='#E65100', linewidth=1)
    ax.add_patch(gear_s)
    ax.text(2.2, 1.8, '10T', fontsize=6, ha='center', va='center', color='#E65100')

    # 馬達
    motor = FancyBboxPatch((2.0, 0.7), 1.0, 0.8, boxstyle="round,pad=0.05",
                           facecolor='#90A4AE', edgecolor='#455A64', linewidth=1.5)
    ax.add_patch(motor)
    ax.text(2.5, 1.1, 'MG996R\n水平馬達', fontsize=7, ha='center', va='center',
            color='white', fontweight='bold')

    # 軸承放大 Detail
    ax.text(0, 6.5, 'Detail A: 軸承安裝', fontsize=10, fontweight='bold', ha='center',
            color='#333', bbox=dict(boxstyle='round', facecolor='#E8F5E9', edgecolor='#4CAF50'))

    detail_items = [
        '軸承外圈 → 固定在轉盤凹槽（熱熔膠）',
        '軸承內圈 → 套住中心軸，可自由轉動',
        '4 顆軸承排成十字 → 轉盤平穩旋轉',
    ]
    for i, item in enumerate(detail_items):
        ax.text(0, 6.0-i*0.35, f'• {item}', fontsize=7, ha='center', color='#555')

    plt.tight_layout()
    plt.savefig(os.path.join(OUT, '004_水平轉動盤詳細圖.png'), dpi=200, bbox_inches='tight',
                facecolor='#FFFEF5')
    plt.close()
    print('004 OK')

# ============================================================
# 005 電路接線圖
# ============================================================
def draw_005():
    fig, ax = plt.subplots(1, 1, figsize=(16, 12))
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 12)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_facecolor('#F5F5F5')
    fig.patch.set_facecolor('#F5F5F5')

    ax.text(8, 11.3, '太陽爐雙軸追日系統 — Arduino 接線圖', fontsize=18,
            fontweight='bold', ha='center', color='#1a5276')

    # --- Arduino UNO ---
    arduino = FancyBboxPatch((0.5, 3.5), 2.5, 4.5, boxstyle="round,pad=0.1",
                             facecolor='#2196F3', edgecolor='#1565C0', linewidth=2)
    ax.add_patch(arduino)
    ax.text(1.75, 7.7, 'Arduino UNO', fontsize=11, ha='center', color='white', fontweight='bold')

    # Arduino pins
    pins_left = [('5V', 7.0), ('GND', 6.5), ('A0', 5.5), ('A1', 5.0),
                 ('A2', 4.5), ('A3', 4.0)]
    for label, y in pins_left:
        pin = plt.Circle((0.5, y), 0.1, facecolor='#FFD700', edgecolor='#333', linewidth=1)
        ax.add_patch(pin)
        ax.text(0.2, y, label, fontsize=6, ha='right', va='center', color='white', fontweight='bold')

    pins_right = [('D9', 6.0), ('D10', 5.5), ('D12', 5.0), ('D13', 4.5)]
    for label, y in pins_right:
        pin = plt.Circle((3.0, y), 0.1, facecolor='#FFD700', edgecolor='#333', linewidth=1)
        ax.add_patch(pin)
        ax.text(3.3, y, label, fontsize=6, ha='left', va='center', color='white', fontweight='bold')

    # --- 麵包板 ---
    bread = FancyBboxPatch((4, 3), 8, 5, boxstyle="round,pad=0.1",
                           facecolor='#FAFAFA', edgecolor='#BDBDBD', linewidth=2)
    ax.add_patch(bread)
    ax.text(8, 7.8, '麵包板 (400孔)', fontsize=10, ha='center', color='#757575', fontweight='bold')

    # 電源軌
    ax.plot([4.2, 11.8], [7.3, 7.3], color='red', linewidth=2)
    ax.text(12.0, 7.3, '+5V', fontsize=7, color='red', fontweight='bold', va='center')
    ax.plot([4.2, 11.8], [3.3, 3.3], color='black', linewidth=2)
    ax.text(12.0, 3.3, 'GND', fontsize=7, color='black', fontweight='bold', va='center')

    # --- LDR ×4 ---
    ldr_names = ['左LDR', '右LDR', '上LDR', '下LDR']
    ldr_pins = ['A0', 'A1', 'A2', 'A3']
    ldr_x = [5.0, 6.5, 8.0, 9.5]

    for i, (name, pin, x) in enumerate(zip(ldr_names, ldr_pins, ldr_x)):
        # LDR 符號
        ldr = plt.Circle((x, 6.8), 0.2, facecolor='#FFEB3B', edgecolor='#F57F17', linewidth=1.5)
        ax.add_patch(ldr)
        # 波浪線（LDR 符號）
        theta = np.linspace(0, 2*np.pi, 20)
        ax.plot(x + 0.15*np.cos(theta), 6.8 + 0.15*np.sin(theta), color='#F57F17', linewidth=1)
        ax.text(x, 7.1, name, fontsize=7, ha='center', color='#333', fontweight='bold')

        # 10K 電阻
        res = FancyBboxPatch((x-0.15, 5.8), 0.3, 0.6, boxstyle="round,pad=0.02",
                             facecolor='#FFF9C4', edgecolor='#F57F17', linewidth=1)
        ax.add_patch(res)
        ax.text(x, 6.1, '10K', fontsize=6, ha='center', va='center', color='#E65100')

        # 接線：5V → LDR → 電阻 → GND
        ax.plot([x, x], [7.3, 7.0], color='red', linewidth=1.5)  # 5V 到 LDR
        ax.plot([x, x], [6.6, 6.4], color='#2196F3', linewidth=1.5)  # LDR 到電阻
        ax.plot([x, x], [5.8, 3.3], color='black', linewidth=1.5)  # 電阻到 GND

        # 分壓點 → Arduino
        ax.plot([x, x], [6.2, 6.2], color='#4CAF50', linewidth=2, marker='o', markersize=4)
        # 連到 Arduino A0~A3
        ax.annotate('', xy=(0.5, 5.5-i*0.5), xytext=(x, 6.2),
                    arrowprops=dict(arrowstyle='->', color='#4CAF50', lw=1.5))
        ax.text((x+0.5)/2, 5.9-i*0.25, pin, fontsize=6, color='#4CAF50', fontweight='bold')

    # --- 伺服馬達 ×2 ---
    # 水平馬達
    motor_h = FancyBboxPatch((11.5, 5.5), 1.8, 1.2, boxstyle="round,pad=0.08",
                             facecolor='#90A4AE', edgecolor='#455A64', linewidth=2)
    ax.add_patch(motor_h)
    ax.text(12.4, 6.4, '水平', fontsize=8, ha='center', color='white', fontweight='bold')
    ax.text(12.4, 6.1, 'MG996R', fontsize=7, ha='center', color='white')
    ax.text(12.4, 5.8, 'D9', fontsize=7, ha='center', color='#FFD700', fontweight='bold')

    # 連接線 D9 → 水平馬達
    ax.plot([3.0, 11.5], [6.0, 6.1], color='#FF9800', linewidth=2, linestyle='-')

    # 垂直馬達
    motor_v = FancyBboxPatch((11.5, 4.0), 1.8, 1.2, boxstyle="round,pad=0.08",
                             facecolor='#90A4AE', edgecolor='#455A64', linewidth=2)
    ax.add_patch(motor_v)
    ax.text(12.4, 4.9, '垂直', fontsize=8, ha='center', color='white', fontweight='bold')
    ax.text(12.4, 4.6, 'MG996R', fontsize=7, ha='center', color='white')
    ax.text(12.4, 4.3, 'D10', fontsize=7, ha='center', color='#FFD700', fontweight='bold')

    # 連接線 D10 → 垂直馬達
    ax.plot([3.0, 11.5], [5.5, 4.6], color='#FF9800', linewidth=2, linestyle='-')

    # --- LED ---
    # 紅色 LED (D13)
    led_r = plt.Circle((5, 4.2), 0.15, facecolor='#F44336', edgecolor='#B71C1C', linewidth=1.5)
    ax.add_patch(led_r)
    ax.text(5, 3.8, '紅LED\nD13', fontsize=6, ha='center', color='#B71C1C')
    ax.plot([3.0, 5], [4.5, 4.35], color='#F44336', linewidth=1.5)

    # 綠色 LED (D12)
    led_g = plt.Circle((6, 4.2), 0.15, facecolor='#4CAF50', edgecolor='#1B5E20', linewidth=1.5)
    ax.add_patch(led_g)
    ax.text(6, 3.8, '綠LED\nD12', fontsize=6, ha='center', color='#1B5E20')
    ax.plot([3.0, 6], [5.0, 4.35], color='#4CAF50', linewidth=1.5)

    # --- 外接電源 ---
    ps = FancyBboxPatch((11.5, 2.0), 1.8, 1.0, boxstyle="round,pad=0.08",
                        facecolor='#424242', edgecolor='#212121', linewidth=2)
    ax.add_patch(ps)
    ax.text(12.4, 2.7, '外接電源', fontsize=7, ha='center', color='white', fontweight='bold')
    ax.text(12.4, 2.3, '5V 2A', fontsize=8, ha='center', color='#FFD700', fontweight='bold')

    # 電源連接線
    ax.plot([11.5, 11.8], [2.5, 3.3], color='black', linewidth=2)  # GND
    ax.plot([11.5, 11.8], [2.8, 7.3], color='red', linewidth=2)  # +5V

    # --- 開關 ---
    sw = FancyBboxPatch((10.5, 2.3), 0.8, 0.4, boxstyle="round,pad=0.05",
                        facecolor='#F44336', edgecolor='#B71C1C', linewidth=1.5)
    ax.add_patch(sw)
    ax.text(10.9, 2.5, '開關', fontsize=6, ha='center', color='white', fontweight='bold')

    # --- 電源系統說明 ---
    notes = [
        '電源系統：',
        '• Arduino 吃 USB 或 DC Jack 供電',
        '• 伺服馬達從外接 5V 2A 供電（不可吃 Arduino 5V！）',
        '• 所有 GND 要接在一起',
    ]
    for i, note in enumerate(notes):
        ax.text(0.5, 2.5-i*0.3, note, fontsize=7, color='#333')

    plt.tight_layout()
    plt.savefig(os.path.join(OUT, '005_電路接線圖.png'), dpi=200, bbox_inches='tight',
                facecolor='#F5F5F5')
    plt.close()
    print('005 OK')

# ============================================================
# 006 完成作品圖
# ============================================================
def draw_006():
    fig, ax = plt.subplots(1, 1, figsize=(16, 12))
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 12)
    ax.set_aspect('equal')
    ax.axis('off')

    # 背景（漸層天空）
    for y in range(120):
        r = 0.53 + (y/120)*0.4
        g = 0.81 + (y/120)*0.15
        b = 0.92 + (y/120)*0.08
        ax.axhspan(y/10, (y+1)/10, color=(r, g, b))

    # 草地
    ax.axhspan(0, 3, color='#8BC34A', alpha=0.5)
    ax.axhspan(0, 2.5, color='#689F38', alpha=0.3)

    # 太陽
    sun = plt.Circle((3, 10), 0.8, facecolor='#FFD700', edgecolor='#FFA000', linewidth=3)
    ax.add_patch(sun)
    # 光線
    for angle in range(0, 360, 30):
        rad = np.radians(angle)
        ax.plot([3 + 1.0*np.cos(rad), 3 + 1.5*np.cos(rad)],
                [10 + 1.0*np.sin(rad), 10 + 1.5*np.sin(rad)],
                color='#FFD700', linewidth=2, alpha=0.6)

    # 標題
    ax.text(8, 11.3, '太陽爐雙軸追日系統 — 完成作品示意圖', fontsize=16,
            fontweight='bold', ha='center', color='#1a5276',
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

    # --- 木桌 ---
    table_top = FancyBboxPatch((2, 2.5), 10, 0.4, boxstyle="round,pad=0.05",
                               facecolor='#8D6E63', edgecolor='#5D4037', linewidth=2)
    ax.add_patch(table_top)
    # 桌腳
    for x in [3, 11]:
        leg = FancyBboxPatch((x-0.15, 0.5), 0.3, 2.0, boxstyle="round,pad=0.02",
                             facecolor='#8D6E63', edgecolor='#5D4037', linewidth=1.5)
        ax.add_patch(leg)

    # --- 底座 ---
    base = FancyBboxPatch((4, 3.0), 5, 0.4, boxstyle="round,pad=0.05",
                          facecolor='#DEB887', edgecolor='#8B4513', linewidth=2)
    ax.add_patch(base)
    ax.text(6.5, 3.2, '底座', fontsize=7, ha='center', color='#8B4513')

    # --- 轉盤 ---
    tt = FancyBboxPatch((4.3, 3.6), 4.4, 0.3, boxstyle="round,pad=0.03",
                        facecolor='#F5DEB3', edgecolor='#8B4513', linewidth=1.5)
    ax.add_patch(tt)

    # --- 立柱 ---
    for x in [5.0, 8.2]:
        col = FancyBboxPatch((x-0.1, 3.9), 0.2, 2.5, boxstyle="round,pad=0.02",
                             facecolor='#DEB887', edgecolor='#8B4513', linewidth=1.5)
        ax.add_patch(col)

    # --- 太陽爐 ---
    theta = np.linspace(-0.7, 0.7, 40)
    xf = 6.6 + 1.8 * np.sin(theta)
    yf = 5.8 + 1.2 * np.cos(theta) * 0.5
    ax.plot(xf, yf, color='#4FC3F7', linewidth=3)
    ax.fill_between(xf, yf, yf-0.12, color='#B3E5FC', alpha=0.7)
    # 鏡面反光
    for i in range(8):
        idx = min(i*5, len(xf)-1)
        ax.plot([xf[idx], 6.6], [yf[idx], 7.5],
                color='#E3F2FD', linewidth=0.8, alpha=0.6)

    ax.text(6.6, 7.5, '拋物面反射鏡', fontsize=8, ha='center', color='#0277BD', fontweight='bold')

    # 光線集中到焦點
    for dx in [-1.5, -0.8, 0, 0.8, 1.5]:
        ax.annotate('', xy=(6.6, 6.8), xytext=(6.6+dx, 8.5),
                    arrowprops=dict(arrowstyle='->', color='#FF9800', lw=1.5, alpha=0.7))

    # 焦點 + 鍋子
    ax.plot(6.6, 6.8, marker='*', markersize=12, color='#FF4500')
    pot = FancyBboxPatch((6.3, 6.9), 0.6, 0.4, boxstyle="round,pad=0.03",
                         facecolor='#757575', edgecolor='#424242', linewidth=1.5)
    ax.add_patch(pot)
    ax.text(6.6, 7.1, '鍋', fontsize=6, ha='center', va='center', color='white')
    ax.text(6.6, 6.5, '焦點', fontsize=7, ha='center', color='#FF4500')

    # --- 水平馬達 ---
    m_h = FancyBboxPatch((4.5, 3.3), 0.6, 0.4, boxstyle="round,pad=0.03",
                         facecolor='#90A4AE', edgecolor='#455A64', linewidth=1)
    ax.add_patch(m_h)

    # --- 垂直馬達 ---
    m_v = FancyBboxPatch((8.3, 4.5), 0.4, 0.5, boxstyle="round,pad=0.03",
                         facecolor='#90A4AE', edgecolor='#455A64', linewidth=1)
    ax.add_patch(m_v)

    # --- Arduino ---
    arduino = FancyBboxPatch((4.0, 3.8), 0.8, 0.5, boxstyle="round,pad=0.03",
                             facecolor='#2196F3', edgecolor='#1565C0', linewidth=1)
    ax.add_patch(arduino)
    ax.text(4.4, 4.05, 'Arduino', fontsize=5, ha='center', color='white')

    # 麵包板
    bread = FancyBboxPatch((5.0, 3.8), 1.0, 0.5, boxstyle="round,pad=0.03",
                           facecolor='#FAFAFA', edgecolor='#BDBDBD', linewidth=1)
    ax.add_patch(bread)
    ax.text(5.5, 4.05, '麵包板', fontsize=5, ha='center', color='#757575')

    # --- 標籤 ---
    labels = [
        (6.6, 8.0, '拋物面反射鏡 (18片式)', '#0277BD'),
        (2.0, 5.0, '水平旋轉\n360°', '#E53935'),
        (10.5, 5.0, '垂直翻轉\n0°~80°', '#E53935'),
        (10.5, 3.5, '水平 MG996R\n伺服馬達', '#455A64'),
        (9.5, 5.5, '垂直 MG996R\n伺服馬達', '#455A64'),
        (5.5, 4.6, 'Arduino 控制系統', '#1565C0'),
        (6.6, 6.0, '光敏電阻 (LDR)', '#F57F17'),
    ]
    for x, y, text, color in labels:
        ax.text(x, y, text, fontsize=7, ha='center', color=color, fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.2', facecolor='white', alpha=0.7, edgecolor=color))

    # 旋轉箭頭
    theta_arr = np.linspace(0, np.pi*1.5, 30)
    ax.plot(6.5 + 2.5*np.cos(theta_arr), 3.5 + 0.3*np.sin(theta_arr)*5,
            color='#E53935', linewidth=2, alpha=0.5)

    plt.tight_layout()
    plt.savefig(os.path.join(OUT, '006_完成作品圖.png'), dpi=200, bbox_inches='tight')
    plt.close()
    print('006 OK')

# ============================================================
# 執行全部
# ============================================================
draw_001()
draw_002()
draw_003()
draw_004()
draw_005()
draw_006()
print('全部完成！')
