# -*- coding:utf-8 -*-
import pygame
from pygame.locals import *
import sys


def main():
    pygame.init()                                               # Pygameの初期化
    screen = pygame.display.set_mode((300, 200))                # 大きさ600*500の画面を生成
    pygame.display.set_caption("GAME")                          # タイトルバーに表示する文字

    while (1):
        screen.fill((0,0,0))                                    # 画面を黒色に塗りつぶし

        # (0,0)から(80,80)まで線幅5pxで緑色(R=0, G=95, B=0)の直線を描く
        pygame.draw.line(screen, (0,95,0), (0,0), (80,80), 5)   # 直線の描画

        # 左上座標(10,10)、幅80px、高さ50pxの長方形を線幅5pxの緑色(R=0, G=80, B=0)で描く
        pygame.draw.rect(screen,(0,80,0),Rect(10,10,80,50),5)   # 四角形を描画(塗りつぶしなし)
        #pygame.draw.rect(screen,(0,80,0),Rect(10,10,80,50))    # 四角形を描画(塗りつぶし)
        
        # 左上の座標が(50,50)、幅が150、高さが50の矩形に内接する楕円を線幅5pxの緑色(R=0, G=100, B=0)で描く
        pygame.draw.ellipse(screen,(0,100,0),(50,50,200,100),5) # 円を描画(塗りつぶしなし)
        #pygame.draw.ellipse(screen,(0,100,0),(50,50,200,100))     # 円を描画(塗りつぶし)
    
        pygame.display.update()                                 # 画面を更新
        # イベント処理
        for event in pygame.event.get():
            if event.type == QUIT:                              # 閉じるボタンが押されたら終了
                pygame.quit()                                   # Pygameの終了(画面閉じられる)
                sys.exit()


if __name__ == "__main__":
    main()
