
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json
import time
import random
from datetime import datetime

class FarmtonBot:
    def __init__(self):
        """تهيئة البوت مع الإعدادات الأساسية"""
        self.session = requests.Session()
        self.base_url = "https://farmton.auto-crypto.click"
        self.current_plot = 0
        self.max_plots = 9
        self.user_stats = {}
        
        # بيانات HTTP الجديدة المحدثة
        self.http_data = {
            "1": """GET /api/login?ref=undefined HTTP/2
Host: farmton.auto-crypto.click
User-Agent: Mozilla/5.0 (Linux; U; Android 2.2; en-us; Droid Build/FRG22D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1
Accept: application/json, text/plain, */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
X-Window-Telegram: {"initData":"query_id=AAFHHGI5AAAAAEccYjkCmrBH&user=%7B%22id%22%3A962731079%2C%22first_name%22%3A%22%E2%9B%A5-%F0%9D%94%BE_%F0%9D%95%84_%F0%9D%94%B8_%E2%84%9A-%E2%9B%A5%22%2C%22last_name%22%3A%22%22%2C%22username%22%3A%22G_M_A_Q%22%2C%22language_code%22%3A%22ar%22%2C%22allows_write_to_pm%22%3Atrue%2C%22photo_url%22%3A%22https%3A%5C%2F%5C%2Ft.me%5C%2Fi%5C%2Fuserpic%5C%2F320%5C%2FLbR-TBHzDuD6cvqpR5mdaD2NXwXhhaMFMXIMcAKqeas.svg%22%7D&auth_date=1750405669&signature=I2LXbWfpEo_eR91PO8JFM9SewZRxLiPCZ1OZYlhmEoD-dl2qgXDnqqlNEKkxZcT9A7YH4QL-P0oewC6s1Wu1BA&hash=0d9bdb00fbbdaa253b1cec89bb145024479307d680c4f98cf030c7747c8ccc55","initDataUnsafe":{"query_id":"AAFHHGI5AAAAAEccYjkCmrBH","user":{"id":962731079,"first_name":"%E2%9B%A5-%F0%9D%94%BE_%F0%9D%95%84_%F0%9D%94%B8_%E2%84%9A-%E2%9B%A5","last_name":"","username":"G_M_A_Q","language_code":"ar","allows_write_to_pm":true,"photo_url":"https://t.me/i/userpic/320/LbR-TBHzDuD6cvqpR5mdaD2NXwXhhaMFMXIMcAKqeas.svg"},"auth_date":"1750405669","signature":"I2LXbWfpEo_eR91PO8JFM9SewZRxLiPCZ1OZYlhmEoD-dl2qgXDnqqlNEKkxZcT9A7YH4QL-P0oewC6s1Wu1BA","hash":"0d9bdb00fbbdaa253b1cec89bb145024479307d680c4f98cf030c7747c8ccc55"},"version":"8.0","platform":"android","colorScheme":"dark","themeParams":{"bg_color":"#212d3b","section_bg_color":"#1d2733","secondary_bg_color":"#151e27","text_color":"#ffffff","hint_color":"#7d8b99","link_color":"#5eabe1","button_color":"#50a8eb","button_text_color":"#ffffff","header_bg_color":"#242d39","accent_text_color":"#64b5ef","section_header_text_color":"#79c4fc","subtitle_text_color":"#7b8790","destructive_text_color":"#ee686f","section_separator_color":"#0d1218","bottom_bar_bg_color":"#151e27"},"isExpanded":true,"viewportHeight":915,"viewportStableHeight":915,"safeAreaInset":{"top":0,"bottom":0,"left":0,"right":0},"contentSafeAreaInset":{"top":0,"bottom":0,"left":0,"right":0},"isClosingConfirmationEnabled":false,"isVerticalSwipesEnabled":true,"isFullscreen":false,"isOrientationLocked":false,"isActive":true,"headerColor":"#212d3b","backgroundColor":"#212d3b","bottomBarColor":"#151e27","BackButton":{"isVisible":false},"MainButton":{"type":"main","text":"Continue","color":"#50a8eb","textColor":"#ffffff","isVisible":false,"isProgressVisible":false,"isActive":true,"hasShineEffect":false},"SecondaryButton":{"type":"secondary","text":"Cancel","color":"#151e27","textColor":"#50a8eb","isVisible":false,"isProgressVisible":false,"isActive":true,"hasShineEffect":false,"position":"left"},"SettingsButton":{"isVisible":false},"HapticFeedback":{},"CloudStorage":{},"DeviceStorage":{},"SecureStorage":{},"BiometricManager":{"isInited":false,"isBiometricAvailable":false,"biometricType":"unknown","isAccessRequested":false,"isAccessGranted":false,"isBiometricTokenSaved":false,"deviceId":""},"Accelerometer":{"isStarted":false,"x":null,"y":null,"z":null},"DeviceOrientation":{"isStarted":false,"absolute":false,"alpha":null,"beta":null,"gamma":null},"Gyroscope":{"isStarted":false,"x":null,"y":null,"z":null},"LocationManager":{"isInited":false,"isLocationAvailable":false,"isAccessRequested":false,"isAccessGranted":false}}
Referer: https://farmton.auto-crypto.click/market
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
If-None-Match: W/"1b6-1KcoJqm4gRBmpS5hNho6ThHFIDQ"
Te: trailers""",
            
            "2": """POST /api/market/buy-seeds HTTP/2
Host: farmton.auto-crypto.click
User-Agent: Mozilla/5.0 (Linux; U; Android 2.2; en-us; Droid Build/FRG22D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1
Accept: application/json, text/plain, */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
X-Window-Telegram: {"initData":"query_id=AAFHHGI5AAAAAEccYjkCmrBH&user=%7B%22id%22%3A962731079%2C%22first_name%22%3A%22%E2%9B%A5-%F0%9D%94%BE_%F0%9D%95%84_%F0%9D%94%B8_%E2%84%9A-%E2%9B%A5%22%2C%22last_name%22%3A%22%22%2C%22username%22%3A%22G_M_A_Q%22%2C%22language_code%22%3A%22ar%22%2C%22allows_write_to_pm%22%3Atrue%2C%22photo_url%22%3A%22https%3A%5C%2F%5C%2Ft.me%5C%2Fi%5C%2Fuserpic%5C%2F320%5C%2FLbR-TBHzDuD6cvqpR5mdaD2NXwXhhaMFMXIMcAKqeas.svg%22%7D&auth_date=1750405669&signature=I2LXbWfpEo_eR91PO8JFM9SewZRxLiPCZ1OZYlhmEoD-dl2qgXDnqqlNEKkxZcT9A7YH4QL-P0oewC6s1Wu1BA&hash=0d9bdb00fbbdaa253b1cec89bb145024479307d680c4f98cf030c7747c8ccc55","initDataUnsafe":{"query_id":"AAFHHGI5AAAAAEccYjkCmrBH","user":{"id":962731079,"first_name":"%E2%9B%A5-%F0%9D%94%BE_%F0%9D%95%84_%F0%9D%94%B8_%E2%84%9A-%E2%9B%A5","last_name":"","username":"G_M_A_Q","language_code":"ar","allows_write_to_pm":true,"photo_url":"https://t.me/i/userpic/320/LbR-TBHzDuD6cvqpR5mdaD2NXwXhhaMFMXIMcAKqeas.svg"},"auth_date":"1750405669","signature":"I2LXbWfpEo_eR91PO8JFM9SewZRxLiPCZ1OZYlhmEoD-dl2qgXDnqqlNEKkxZcT9A7YH4QL-P0oewC6s1Wu1BA","hash":"0d9bdb00fbbdaa253b1cec89bb145024479307d680c4f98cf030c7747c8ccc55"},"version":"8.0","platform":"android","colorScheme":"dark","themeParams":{"bg_color":"#212d3b","section_bg_color":"#1d2733","secondary_bg_color":"#151e27","text_color":"#ffffff","hint_color":"#7d8b99","link_color":"#5eabe1","button_color":"#50a8eb","button_text_color":"#ffffff","header_bg_color":"#242d39","accent_text_color":"#64b5ef","section_header_text_color":"#79c4fc","subtitle_text_color":"#7b8790","destructive_text_color":"#ee686f","section_separator_color":"#0d1218","bottom_bar_bg_color":"#151e27"},"isExpanded":true,"viewportHeight":915,"viewportStableHeight":915,"safeAreaInset":{"top":0,"bottom":0,"left":0,"right":0},"contentSafeAreaInset":{"top":0,"bottom":0,"left":0,"right":0},"isClosingConfirmationEnabled":false,"isVerticalSwipesEnabled":true,"isFullscreen":false,"isOrientationLocked":false,"isActive":true,"headerColor":"#212d3b","backgroundColor":"#212d3b","bottomBarColor":"#151e27","BackButton":{"isVisible":false},"MainButton":{"type":"main","text":"Continue","color":"#50a8eb","textColor":"#ffffff","isVisible":false,"isProgressVisible":false,"isActive":true,"hasShineEffect":false},"SecondaryButton":{"type":"secondary","text":"Cancel","color":"#151e27","textColor":"#50a8eb","isVisible":false,"isProgressVisible":false,"isActive":true,"hasShineEffect":false,"position":"left"},"SettingsButton":{"isVisible":false},"HapticFeedback":{},"CloudStorage":{},"DeviceStorage":{},"SecureStorage":{},"BiometricManager":{"isInited":false,"isBiometricAvailable":false,"biometricType":"unknown","isAccessRequested":false,"isAccessGranted":false,"isBiometricTokenSaved":false,"deviceId":""},"Accelerometer":{"isStarted":false,"x":null,"y":null,"z":null},"DeviceOrientation":{"isStarted":false,"absolute":false,"alpha":null,"beta":null,"gamma":null},"Gyroscope":{"isStarted":false,"x":null,"y":null,"z":null},"LocationManager":{"isInited":false,"isLocationAvailable":false,"isAccessRequested":false,"isAccessGranted":false}}
Content-Type: application/json
Referer: https://farmton.auto-crypto.click/market
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers

{"amount":9}""",
            
            "3": """POST /api/market/buy-water HTTP/2
Host: farmton.auto-crypto.click
User-Agent: Mozilla/5.0 (Linux; U; Android 2.2; en-us; Droid Build/FRG22D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1
Accept: application/json, text/plain, */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
X-Window-Telegram: {"initData":"query_id=AAFHHGI5AAAAAEccYjkCmrBH&user=%7B%22id%22%3A962731079%2C%22first_name%22%3A%22%E2%9B%A5-%F0%9D%94%BE_%F0%9D%95%84_%F0%9D%94%B8_%E2%84%9A-%E2%9B%A5%22%2C%22last_name%22%3A%22%22%2C%22username%22%3A%22G_M_A_Q%22%2C%22language_code%22%3A%22ar%22%2C%22allows_write_to_pm%22%3Atrue%2C%22photo_url%22%3A%22https%3A%5C%2F%5C%2Ft.me%5C%2Fi%5C%2Fuserpic%5C%2F320%5C%2FLbR-TBHzDuD6cvqpR5mdaD2NXwXhhaMFMXIMcAKqeas.svg%22%7D&auth_date=1750405669&signature=I2LXbWfpEo_eR91PO8JFM9SewZRxLiPCZ1OZYlhmEoD-dl2qgXDnqqlNEKkxZcT9A7YH4QL-P0oewC6s1Wu1BA&hash=0d9bdb00fbbdaa253b1cec89bb145024479307d680c4f98cf030c7747c8ccc55","initDataUnsafe":{"query_id":"AAFHHGI5AAAAAEccYjkCmrBH","user":{"id":962731079,"first_name":"%E2%9B%A5-%F0%9D%94%BE_%F0%9D%95%84_%F0%9D%94%B8_%E2%84%9A-%E2%9B%A5","last_name":"","username":"G_M_A_Q","language_code":"ar","allows_write_to_pm":true,"photo_url":"https://t.me/i/userpic/320/LbR-TBHzDuD6cvqpR5mdaD2NXwXhhaMFMXIMcAKqeas.svg"},"auth_date":"1750405669","signature":"I2LXbWfpEo_eR91PO8JFM9SewZRxLiPCZ1OZYlhmEoD-dl2qgXDnqqlNEKkxZcT9A7YH4QL-P0oewC6s1Wu1BA","hash":"0d9bdb00fbbdaa253b1cec89bb145024479307d680c4f98cf030c7747c8ccc55"},"version":"8.0","platform":"android","colorScheme":"dark","themeParams":{"bg_color":"#212d3b","section_bg_color":"#1d2733","secondary_bg_color":"#151e27","text_color":"#ffffff","hint_color":"#7d8b99","link_color":"#5eabe1","button_color":"#50a8eb","button_text_color":"#ffffff","header_bg_color":"#242d39","accent_text_color":"#64b5ef","section_header_text_color":"#79c4fc","subtitle_text_color":"#7b8790","destructive_text_color":"#ee686f","section_separator_color":"#0d1218","bottom_bar_bg_color":"#151e27"},"isExpanded":true,"viewportHeight":915,"viewportStableHeight":915,"safeAreaInset":{"top":0,"bottom":0,"left":0,"right":0},"contentSafeAreaInset":{"top":0,"bottom":0,"left":0,"right":0},"isClosingConfirmationEnabled":false,"isVerticalSwipesEnabled":true,"isFullscreen":false,"isOrientationLocked":false,"isActive":true,"headerColor":"#212d3b","backgroundColor":"#212d3b","bottomBarColor":"#151e27","BackButton":{"isVisible":false},"MainButton":{"type":"main","text":"Continue","color":"#50a8eb","textColor":"#ffffff","isVisible":false,"isProgressVisible":false,"isActive":true,"hasShineEffect":false},"SecondaryButton":{"type":"secondary","text":"Cancel","color":"#151e27","textColor":"#50a8eb","isVisible":false,"isProgressVisible":false,"isActive":true,"hasShineEffect":false,"position":"left"},"SettingsButton":{"isVisible":false},"HapticFeedback":{},"CloudStorage":{},"DeviceStorage":{},"SecureStorage":{},"BiometricManager":{"isInited":false,"isBiometricAvailable":false,"biometricType":"unknown","isAccessRequested":false,"isAccessGranted":false,"isBiometricTokenSaved":false,"deviceId":""},"Accelerometer":{"isStarted":false,"x":null,"y":null,"z":null},"DeviceOrientation":{"isStarted":false,"absolute":false,"alpha":null,"beta":null,"gamma":null},"Gyroscope":{"isStarted":false,"x":null,"y":null,"z":null},"LocationManager":{"isInited":false,"isLocationAvailable":false,"isAccessRequested":false,"isAccessGranted":false}}
Content-Type: application/json
Referer: https://farmton.auto-crypto.click/market
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers

{"amount":9}""",
            
            "4": """POST /api/crop/plant HTTP/2
Host: farmton.auto-crypto.click
User-Agent: Mozilla/5.0 (Linux; U; Android 2.2; en-us; Droid Build/FRG22D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1
Accept: application/json, text/plain, */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
X-Window-Telegram: {"initData":"query_id=AAFHHGI5AAAAAEccYjkCmrBH&user=%7B%22id%22%3A962731079%2C%22first_name%22%3A%22%E2%9B%A5-%F0%9D%94%BE_%F0%9D%95%84_%F0%9D%94%B8_%E2%84%9A-%E2%9B%A5%22%2C%22last_name%22%3A%22%22%2C%22username%22%3A%22G_M_A_Q%22%2C%22language_code%22%3A%22ar%22%2C%22allows_write_to_pm%22%3Atrue%2C%22photo_url%22%3A%22https%3A%5C%2F%5C%2Ft.me%5C%2Fi%5C%2Fuserpic%5C%2F320%5C%2FLbR-TBHzDuD6cvqpR5mdaD2NXwXhhaMFMXIMcAKqeas.svg%22%7D&auth_date=1750405669&signature=I2LXbWfpEo_eR91PO8JFM9SewZRxLiPCZ1OZYlhmEoD-dl2qgXDnqqlNEKkxZcT9A7YH4QL-P0oewC6s1Wu1BA&hash=0d9bdb00fbbdaa253b1cec89bb145024479307d680c4f98cf030c7747c8ccc55","initDataUnsafe":{"query_id":"AAFHHGI5AAAAAEccYjkCmrBH","user":{"id":962731079,"first_name":"%E2%9B%A5-%F0%9D%94%BE_%F0%9D%95%84_%F0%9D%94%B8_%E2%84%9A-%E2%9B%A5","last_name":"","username":"G_M_A_Q","language_code":"ar","allows_write_to_pm":true,"photo_url":"https://t.me/i/userpic/320/LbR-TBHzDuD6cvqpR5mdaD2NXwXhhaMFMXIMcAKqeas.svg"},"auth_date":"1750405669","signature":"I2LXbWfpEo_eR91PO8JFM9SewZRxLiPCZ1OZYlhmEoD-dl2qgXDnqqlNEKkxZcT9A7YH4QL-P0oewC6s1Wu1BA","hash":"0d9bdb00fbbdaa253b1cec89bb145024479307d680c4f98cf030c7747c8ccc55"},"version":"8.0","platform":"android","colorScheme":"dark","themeParams":{"bg_color":"#212d3b","section_bg_color":"#1d2733","secondary_bg_color":"#151e27","text_color":"#ffffff","hint_color":"#7d8b99","link_color":"#5eabe1","button_color":"#50a8eb","button_text_color":"#ffffff","header_bg_color":"#242d39","accent_text_color":"#64b5ef","section_header_text_color":"#79c4fc","subtitle_text_color":"#7b8790","destructive_text_color":"#ee686f","section_separator_color":"#0d1218","bottom_bar_bg_color":"#151e27"},"isExpanded":true,"viewportHeight":915,"viewportStableHeight":915,"safeAreaInset":{"top":0,"bottom":0,"left":0,"right":0},"contentSafeAreaInset":{"top":0,"bottom":0,"left":0,"right":0},"isClosingConfirmationEnabled":false,"isVerticalSwipesEnabled":true,"isFullscreen":false,"isOrientationLocked":false,"isActive":true,"headerColor":"#212d3b","backgroundColor":"#212d3b","bottomBarColor":"#151e27","BackButton":{"isVisible":false},"MainButton":{"type":"main","text":"Continue","color":"#50a8eb","textColor":"#ffffff","is Visible":false,"isProgressVisible":false,"isActive":true,"hasShineEffect":false},"SecondaryButton":{"type":"secondary","text":"Cancel","color":"#151e27","textColor":"#50a8eb","isVisible":false,"isProgressVisible":false,"isActive":true,"hasShineEffect":false,"position":"left"},"SettingsButton":{"isVisible":false},"HapticFeedback":{},"CloudStorage":{},"DeviceStorage":{},"SecureStorage":{},"BiometricManager":{"isInited":false,"isBiometricAvailable":false,"biometricType":"unknown","isAccessRequested":false,"isAccessGranted":false,"isBiometricTokenSaved":false,"deviceId":""},"Accelerometer":{"isStarted":false,"x":null,"y":null,"z":null},"DeviceOrientation":{"isStarted":false,"absolute":false,"alpha":null,"beta":null,"gamma":null},"Gyroscope":{"isStarted":false,"x":null,"y":null,"z":null},"LocationManager":{"isInited":false,"isLocationAvailable":false,"isAccessRequested":false,"isAccessGranted":false}}
Content-Type: application/json
Referer: https://farmton.auto-crypto.click/market
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers

{"plotIndex":0}""",
            
            "5": """POST /api/crop/water HTTP/2
Host: farmton.auto-crypto.click
User-Agent: Mozilla/5.0 (Linux; U; Android 2.2; en-us; Droid Build/FRG22D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1
Accept: application/json, text/plain, */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
X-Window-Telegram: {"initData":"query_id=AAFHHGI5AAAAAEccYjkCmrBH&user=%7B%22id%22%3A962731079%2C%22first_name%22%3A%22%E2%9B%A5-%F0%9D%94%BE_%F0%9D%95%84_%F0%9D%94%B8_%E2%84%9A-%E2%9B%A5%22%2C%22last_name%22%3A%22%22%2C%22username%22%3A%22G_M_A_Q%22%2C%22language_code%22%3A%22ar%22%2C%22allows_write_to_pm%22%3Atrue%2C%22photo_url%22%3A%22https%3A%5C%2F%5C%2Ft.me%5C%2Fi%5C%2Fuserpic%5C%2F320%5C%2FLbR-TBHzDuD6cvqpR5mdaD2NXwXhhaMFMXIMcAKqeas.svg%22%7D&auth_date=1750405669&signature=I2LXbWfpEo_eR91PO8JFM9SewZRxLiPCZ1OZYlhmEoD-dl2qgXDnqqlNEKkxZcT9A7YH4QL-P0oewC6s1Wu1BA&hash=0d9bdb00fbbdaa253b1cec89bb145024479307d680c4f98cf030c7747c8ccc55","initDataUnsafe":{"query_id":"AAFHHGI5AAAAAEccYjkCmrBH","user":{"id":962731079,"first_name":"%E2%9B%A5-%F0%9D%94%BE_%F0%9D%95%84_%F0%9D%94%B8_%E2%84%9A-%E2%9B%A5","last_name":"","username":"G_M_A_Q","language_code":"ar","allows_write_to_pm":true,"photo_url":"https://t.me/i/userpic/320/LbR-TBHzDuD6cvqpR5mdaD2NXwXhhaMFMXIMcAKqeas.svg"},"auth_date":"1750405669","signature":"I2LXbWfpEo_eR91PO8JFM9SewZRxLiPCZ1OZYlhmEoD-dl2qgXDnqqlNEKkxZcT9A7YH4QL-P0oewC6s1Wu1BA","hash":"0d9bdb00fbbdaa253b1cec89bb145024479307d680c4f98cf030c7747c8ccc55"},"version":"8.0","platform":"android","colorScheme":"dark","themeParams":{"bg_color":"#212d3b","section_bg_color":"#1d2733","secondary_bg_color":"#151e27","text_color":"#ffffff","hint_color":"#7d8b99","link_color":"#5eabe1","button_color":"#50a8eb","button_text_color":"#ffffff","header_bg_color":"#242d39","accent_text_color":"#64b5ef","section_header_text_color":"#79c4fc","subtitle_text_color":"#7b8790","destructive_text_color":"#ee686f","section_separator_color":"#0d1218","bottom_bar_bg_color":"#151e27"},"isExpanded":true,"viewportHeight":915,"viewportStableHeight":915,"safeAreaInset":{"top":0,"bottom":0,"left":0,"right":0},"contentSafeAreaInset":{"top":0,"bottom":0,"left":0,"right":0},"isClosingConfirmationEnabled":false,"isVerticalSwipesEnabled":true,"isFullscreen":false,"isOrientationLocked":false,"isActive":true,"headerColor":"#212d3b","backgroundColor":"#212d3b","bottomBarColor":"#151e27","BackButton":{"isVisible":false},"MainButton":{"type":"main","text":"Continue","color":"#50a8eb","textColor":"#ffffff","isVisible":false,"isProgressVisible":false,"isActive":true,"hasShineEffect":false},"SecondaryButton":{"type":"secondary","text":"Cancel","color":"#151e27","textColor":"#50a8eb","isVisible":false,"isProgressVisible":false,"isActive":true,"hasShineEffect":false,"position":"left"},"SettingsButton":{"isVisible":false},"HapticFeedback":{},"CloudStorage":{},"DeviceStorage":{},"SecureStorage":{},"BiometricManager":{"isInited":false,"isBiometricAvailable":false,"biometricType":"unknown","isAccessRequested":false,"isAccessGranted":false,"isBiometricTokenSaved":false,"deviceId":""},"Accelerometer":{"isStarted":false,"x":null,"y":null,"z":null},"DeviceOrientation":{"isStarted":false,"absolute":false,"alpha":null,"beta":null,"gamma":null},"Gyroscope":{"isStarted":false,"x":null,"y":null,"z":null},"LocationManager":{"isInited":false,"isLocationAvailable":false,"isAccessRequested":false,"isAccessGranted":false}}
Content-Type: application/json
Referer: https://farmton.auto-crypto.click/market
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers

{"plotIndex":0}""",
            
            "6": """POST /api/crop/harvest HTTP/2
Host: farmton.auto-crypto.click
User-Agent: Mozilla/5.0 (Linux; U; Android 2.2; en-us; Droid Build/FRG22D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1
Accept: application/json, text/plain, */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
X-Window-Telegram: {"initData":"query_id=AAFHHGI5AAAAAEccYjkCmrBH&user=%7B%22id%22%3A962731079%2C%22first_name%22%3A%22%E2%9B%A5-%F0%9D%94%BE_%F0%9D%95%84_%F0%9D%94%B8_%E2%84%9A-%E2%9B%A5%22%2C%22last_name%22%3A%22%22%2C%22username%22%3A%22G_M_A_Q%22%2C%22language_code%22%3A%22ar%22%2C%22allows_write_to_pm%22%3Atrue%2C%22photo_url%22%3A%22https%3A%5C%2F%5C%2Ft.me%5C%2Fi%5C%2Fuserpic%5C%2F320%5C%2FLbR-TBHzDuD6cvqpR5mdaD2NXwXhhaMFMXIMcAKqeas.svg%22%7D&auth_date=1750405669&signature=I2LXbWfpEo_eR91PO8JFM9SewZRxLiPCZ1OZYlhmEoD-dl2qgXDnqqlNEKkxZcT9A7YH4QL-P0oewC6s1Wu1BA&hash=0d9bdb00fbbdaa253b1cec89bb145024479307d680c4f98cf030c7747c8ccc55","initDataUnsafe":{"query_id":"AAFHHGI5AAAAAEccYjkCmrBH","user":{"id":962731079,"first_name":"%E2%9B%A5-%F0%9D%94%BE_%F0%9D%95%84_%F0%9D%94%B8_%E2%84%9A-%E2%9B%A5","last_name":"","username":"G_M_A_Q","language_code":"ar","allows_write_to_pm":true,"photo_url":"https://t.me/i/userpic/320/LbR-TBHzDuD6cvqpR5mdaD2NXwXhhaMFMXIMcAKqeas.svg"},"auth_date":"1750405669","signature":"I2LXbWfpEo_eR91PO8JFM9SewZRxLiPCZ1OZYlhmEoD-dl2qgXDnqqlNEKkxZcT9A7YH4QL-P0oewC6s1Wu1BA","hash":"0d9bdb00fbbdaa253b1cec89bb145024479307d680c4f98cf030c7747c8ccc55"},"version":"8.0","platform":"android","colorScheme":"dark","themeParams":{"bg_color":"#212d3b","section_bg_color":"#1d2733","secondary_bg_color":"#151e27","text_color":"#ffffff","hint_color":"#7d8b99","link_color":"#5eabe1","button_color":"#50a8eb","button_text_color":"#ffffff","header_bg_color":"#242d39","accent_text_color":"#64b5ef","section_header_text_color":"#79c4fc","subtitle_text_color":"#7b8790","destructive_text_color":"#ee686f","section_separator_color":"#0d1218","bottom_bar_bg_color":"#151e27"},"isExpanded":true,"viewportHeight":915,"viewportStableHeight":915,"safeAreaInset":{"top":0,"bottom":0,"left":0,"right":0},"contentSafeAreaInset":{"top":0,"bottom":0,"left":0,"right":0},"isClosingConfirmationEnabled":false,"isVerticalSwipesEnabled":true,"isFullscreen":false,"isOrientationLocked":false,"isActive":true,"headerColor":"#212d3b","backgroundColor":"#212d3b","bottomBarColor":"#151e27","BackButton":{"isVisible":false},"MainButton":{"type":"main","text":"Continue","color":"#50a8eb","textColor":"#ffffff","isVisible":false,"isProgressVisible":false,"isActive":true,"hasShineEffect":false},"SecondaryButton":{"type":"secondary","text":"Cancel","color":"#151e27","textColor":"#50a8eb","isVisible":false,"isProgressVisible":false,"isActive":true,"hasShineEffect":false,"position":"left"},"SettingsButton":{"isVisible":false},"HapticFeedback":{},"CloudStorage":{},"DeviceStorage":{},"SecureStorage":{},"BiometricManager":{"isInited":false,"isBiometricAvailable":false,"biometricType":"unknown","isAccessRequested":false,"isAccessGranted":false,"isBiometricTokenSaved":false,"deviceId":""},"Accelerometer":{"isStarted":false,"x":null,"y":null,"z":null},"DeviceOrientation":{"isStarted":false,"absolute":false,"alpha":null,"beta":null,"gamma":null},"Gyroscope":{"isStarted":false,"x":null,"y":null,"z":null},"LocationManager":{"isInited":false,"isLocationAvailable":false,"isAccessRequested":false,"isAccessGranted":false}}
Content-Type: application/json
Referer: https://farmton.auto-crypto.click/market
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers

{"plotIndex":0}""",
            
            "7": """POST /api/market/sell-wheat HTTP/2
Host: farmton.auto-crypto.click
User-Agent: Mozilla/5.0 (Linux; U; Android 2.2; en-us; Droid Build/FRG22D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1
Accept: application/json, text/plain, */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
X-Window-Telegram: {"initData":"query_id=AAFHHGI5AAAAAEccYjkCmrBH&user=%7B%22id%22%3A962731079%2C%22first_name%22%3A%22%E2%9B%A5-%F0%9D%94%BE_%F0%9D%95%84_%F0%9D%94%B8_%E2%84%9A-%E2%9B%A5%22%2C%22last_name%22%3A%22%22%2C%22username%22%3A%22G_M_A_Q%22%2C%22language_code%22%3A%22ar%22%2C%22allows_write_to_pm%22%3Atrue%2C%22photo_url%22%3A%22https%3A%5C%2F%5C%2Ft.me%5C%2Fi%5C%2Fuserpic%5C%2F320%5C%2FLbR-TBHzDuD6cvqpR5mdaD2NXwXhhaMFMXIMcAKqeas.svg%22%7D&auth_date=1750405669&signature=I2LXbWfpEo_eR91PO8JFM9SewZRxLiPCZ1OZYlhmEoD-dl2qgXDnqqlNEKkxZcT9A7YH4QL-P0oewC6s1Wu1BA&hash=0d9bdb00fbbdaa253b1cec89bb145024479307d680c4f98cf030c7747c8ccc55","initDataUnsafe":{"query_id":"AAFHHGI5AAAAAEccYjkCmrBH","user":{"id":962731079,"first_name":"%E2%9B%A5-%F0%9D%94%BE_%F0%9D%95%84_%F0%9D%94%B8_%E2%84%9A-%E2%9B%A5","last_name":"","username":"G_M_A_Q","language_code":"ar","allows_write_to_pm":true,"photo_url":"https://t.me/i/userpic/320/LbR-TBHzDuD6cvqpR5mdaD2NXwXhhaMFMXIMcAKqeas.svg"},"auth_date":"1750405669","signature":"I2LXbWfpEo_eR91PO8JFM9SewZRxLiPCZ1OZYlhmEoD-dl2qgXDnqqlNEKkxZcT9A7YH4QL-P0oewC6s1Wu1BA","hash":"0d9bdb00fbbdaa253b1cec89bb145024479307d680c4f98cf030c7747c8ccc55"},"version":"8.0","platform":"android","colorScheme":"dark","themeParams":{"bg_color":"#212d3b","section_bg_color":"#1d2733","secondary_bg_color":"#151e27","text_color":"#ffffff","hint_color":"#7d8b99","link_color":"#5eabe1","button_color":"#50a8eb","button_text_color":"#ffffff","header_bg_color":"#242d39","accent_text_color":"#64b5ef","section_header_text_color":"#79c4fc","subtitle_text_color":"#7b8790","destructive_text_color":"#ee686f","section_separator_color":"#0d1218","bottom_bar_bg_color":"#151e27"},"isExpanded":true,"viewportHeight":915,"viewportStableHeight":915,"safeAreaInset":{"top":0,"bottom":0,"left":0,"right":0},"contentSafeAreaInset":{"top":0,"bottom":0,"left":0,"right":0},"isClosingConfirmationEnabled":false,"isVerticalSwipesEnabled":true,"isFullscreen":false,"isOrientationLocked":false,"isActive":true,"headerColor":"#212d3b","backgroundColor":"#212d3b","bottomBarColor":"#151e27","BackButton":{"isVisible":false},"MainButton":{"type":"main","text":"Continue","color":"#50a8eb","textColor":"#ffffff","isVisible":false,"isProgressVisible":false,"isActive":true,"hasShineEffect":false},"SecondaryButton":{"type":"secondary","text":"Cancel","color":"#151e27","textColor":"#50a8eb","isVisible":false,"isProgressVisible":false,"isActive":true,"hasShineEffect":false,"position":"left"},"SettingsButton":{"isVisible":false},"HapticFeedback":{},"CloudStorage":{},"DeviceStorage":{},"SecureStorage":{},"BiometricManager":{"isInited":false,"isBiometricAvailable":false,"biometricType":"unknown","isAccessRequested":false,"isAccessGranted":false,"isBiometricTokenSaved":false,"deviceId":""},"Accelerometer":{"isStarted":false,"x":null,"y":null,"z":null},"DeviceOrientation":{"isStarted":false,"absolute":false,"alpha":null,"beta":null,"gamma":null},"Gyroscope":{"isStarted":false,"x":null,"y":null,"z":null},"LocationManager":{"isInited":false,"isLocationAvailable":false,"isAccessRequested":false,"isAccessGranted":false}}
Content-Type: application/json
Referer: https://farmton.auto-crypto.click/market
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers

{"amount":1}"""
        }
        
        print("✅ تم تحديث بيانات التوثيق بنجاح!")
        print("🚀 البوت جاهز للتشغيل بالبيانات الجديدة!")
        print("=" * 50)

    def parse_http_data(self, file_key):
        """تحليل بيانات HTTP من الملف المدمج"""
        if file_key not in self.http_data:
            print(f"❌ الملف {file_key} غير موجود")
            return None

        http_content = self.http_data[file_key]
        lines = http_content.strip().split('\n')
        
        # تحليل السطر الأول للحصول على HTTP method و URL
        first_line = lines[0].strip()
        parts = first_line.split(' ')
        method = parts[0]
        path = parts[1]
        
        # تحليل الهيدرز
        headers = {}
        body_start = -1
        
        for i, line in enumerate(lines[1:], 1):
            line = line.strip()
            if line == '':
                body_start = i + 1
                break
            if ':' in line:
                key, value = line.split(':', 1)
                headers[key.strip()] = value.strip()
        
        # تحليل الـ body إذا وجد
        body = None
        if body_start != -1 and body_start < len(lines):
            body_lines = lines[body_start:]
            if body_lines:
                body = '\n'.join(body_lines).strip()
        
        return {
            'method': method,
            'url': f"{self.base_url}{path}",
            'headers': headers,
            'body': body
        }

    def execute_request(self, request_data, custom_body=None):
        """تنفيذ طلب HTTP"""
        try:
            url = request_data['url']
            method = request_data['method']
            headers = request_data['headers'].copy()
            body = custom_body if custom_body else request_data['body']
            
            print(f"🔄 تنفيذ طلب: {method} {url}")
            
            if method == 'GET':
                response = self.session.get(url, headers=headers, timeout=30)
            elif method == 'POST':
                response = self.session.post(url, headers=headers, data=body, timeout=30)
            else:
                print(f"❌ طريقة HTTP غير مدعومة: {method}")
                return False
            
            print(f"✅ رد الخادم: {response.status_code}")
            
            if response.status_code == 200:
                try:
                    response_json = response.json()
                    return response_json
                except:
                    return True
            else:
                print(f"❌ خطأ من الخادم: {response.status_code}")
                try:
                    error_response = response.json()
                    print(f"📝 الرد: {json.dumps(error_response, ensure_ascii=False)}")
                except:
                    print(f"📝 الرد: {response.text}")
                return False
                
        except requests.exceptions.RequestException as e:
            print(f"❌ خطأ في الشبكة: {e}")
            return False
        except Exception as e:
            print(f"❌ خطأ عام: {e}")
            return False

    def get_user_stats(self):
        """الحصول على إحصائيات المستخدم"""
        request_data = self.parse_http_data("1")
        if not request_data:
            return None
            
        response = self.execute_request(request_data)
        
        if response and isinstance(response, dict):
            self.user_stats = response
            return response
        else:
            print("❌ فشل في الحصول على إحصائيات المستخدم")
            return None

    def display_stats(self):
        """عرض إحصائيات المستخدم"""
        if not self.user_stats:
            return
            
        print("=" * 50)
        print("📊 إحصائيات المستخدم الحالية:")
        print(f"👤 اسم المستخدم: {self.user_stats.get('username', 'غير محدد')}")
        print(f"💰 العملات: {self.user_stats.get('coins', 0)}")
        print(f"🌾 القمح: {self.user_stats.get('wheat', 0)}")
        print(f"🌱 البذور: {self.user_stats.get('seeds', 0)}")
        print(f"💧 الماء: {self.user_stats.get('water', 0)}")
        print("=" * 50)

    def buy_seeds(self, amount=1):
        """شراء البذور"""
        print(f"🌱 جاري شراء {amount} بذرة...")
        request_data = self.parse_http_data("2")
        if not request_data:
            return False
            
        custom_body = json.dumps({"amount": amount})
        response = self.execute_request(request_data, custom_body)
        
        if response:
            print(f"✅ تم شراء {amount} بذرة بنجاح")
            return True
        else:
            print("❌ فشل في شراء البذور")
            return False

    def buy_water(self, amount=1):
        """شراء الماء"""
        print(f"💧 جاري شراء {amount} وحدة ماء...")
        request_data = self.parse_http_data("3")
        if not request_data:
            return False
            
        custom_body = json.dumps({"amount": amount})
        response = self.execute_request(request_data, custom_body)
        
        if response:
            print(f"✅ تم شراء {amount} وحدة ماء بنجاح")
            return True
        else:
            print("❌ فشل في شراء الماء")
            return False

    def plant_crop(self, plot_index):
        """زراعة المحصول في قطعة أرض معينة"""
        print(f"🌱 جاري زراعة الأرض رقم {plot_index}...")
        request_data = self.parse_http_data("4")
        if not request_data:
            return False
            
        custom_body = json.dumps({"plotIndex": plot_index})
        response = self.execute_request(request_data, custom_body)
        
        if response:
            print(f"✅ تم زراعة الأرض رقم {plot_index} بنجاح")
            return True
        else:
            print(f"❌ فشل في زراعة الأرض رقم {plot_index}")
            return False

    def water_crop(self, plot_index):
        """ري المحصول في قطعة أرض معينة"""
        print(f"💧 جاري ري الأرض رقم {plot_index}...")
        request_data = self.parse_http_data("5")
        if not request_data:
            return False
            
        custom_body = json.dumps({"plotIndex": plot_index})
        response = self.execute_request(request_data, custom_body)
        
        if response:
            print(f"✅ تم ري الأرض رقم {plot_index} بنجاح")
            return True
        else:
            print(f"❌ فشل في ري الأرض رقم {plot_index}")
            return False

    def harvest_crop(self, plot_index):
        """حصاد المحصول من قطعة أرض معينة"""
        print(f"🌾 جاري حصاد الأرض رقم {plot_index}...")
        request_data = self.parse_http_data("6")
        if not request_data:
            return False
            
        custom_body = json.dumps({"plotIndex": plot_index})
        response = self.execute_request(request_data, custom_body)
        
        if response:
            print(f"✅ تم حصاد الأرض رقم {plot_index} بنجاح")
            return True
        else:
            print(f"❌ فشل في حصاد الأرض رقم {plot_index}")
            return False

    def sell_wheat(self, amount):
        """بيع القمح"""
        print(f"💰 جاري بيع {amount} وحدة قمح...")
        request_data = self.parse_http_data("7")
        if not request_data:
            return False
            
        custom_body = json.dumps({"amount": amount})
        response = self.execute_request(request_data, custom_body)
        
        if response:
            print(f"✅ تم بيع {amount} وحدة قمح بنجاح")
            return True
        else:
            print("❌ فشل في بيع القمح")
            return False

    def farming_cycle(self, plot_index):
        """دورة زراعة كاملة لأرض واحدة"""
        print(f"🚜 بدء دورة زراعة للأرض {plot_index}...")
        
        # شراء البذور والماء
        if not self.buy_seeds(1):
            return False
        time.sleep(2)
        
        if not self.buy_water(1):
            return False
        time.sleep(2)
        
        # زراعة
        if not self.plant_crop(plot_index):
            return False
        time.sleep(2)
        
        # ري
        if not self.water_crop(plot_index):
            return False
        time.sleep(2)
        
        # انتظار نضج المحصول
        print("⏳ انتظار نضج المحصول (45 ثانية)...")
        time.sleep(45)
        
        # حصاد
        if not self.harvest_crop(plot_index):
            return False
        
        print(f"✅ تم إنجاز دورة زراعة الأرض {plot_index} بنجاح")
        return True

    def run_automation(self):
        """تشغيل الأتمتة الرئيسية"""
        print("🤖 بدء تشغيل بوت Farmton...")
        print("⚠️ اضغط Ctrl+C لإيقاف البوت")
        
        cycle_count = 0
        
        try:
            while True:
                cycle_count += 1
                print(f"🔄 بدء الدورة رقم {cycle_count}")
                print(f"⏰ {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                
                # الحصول على الإحصائيات
                print("📊 جاري الحصول على إحصائيات المستخدم...")
                if not self.get_user_stats():
                    print("❌ فشل في الحصول على الإحصائيات - انتظار 30 ثانية...")
                    time.sleep(30)
                    continue
                
                self.display_stats()
                
                # التحقق من وجود قمح للبيع
                wheat = self.user_stats.get('wheat', 0)
                if wheat > 0:
                    print(f"💰 بيع {wheat} وحدة قمح...")
                    self.sell_wheat(wheat)
                    time.sleep(3)
                    continue
                
                # تشغيل دورة زراعة للأرض الحالية
                if self.farming_cycle(self.current_plot):
                    print(f"✅ تم إنجاز زراعة الأرض {self.current_plot}")
                    # الانتقال للأرض التالية
                    self.current_plot = (self.current_plot + 1) % self.max_plots
                    print(f"📍 الأرض التالية: {self.current_plot}")
                else:
                    print(f"❌ فشل في زراعة الأرض {self.current_plot}")
                
                print("✅ انتهاء الدورة - انتظار 10 ثواني قبل الدورة التالية")
                time.sleep(10)
                
        except KeyboardInterrupt:
            print("\n⛔ تم إيقاف البوت بواسطة المستخدم")
        except Exception as e:
            print(f"❌ خطأ غير متوقع: {e}")
            print("🔄 إعادة المحاولة خلال 30 ثانية...")
            time.sleep(30)

def main():
    """الدالة الرئيسية"""
    print("🌾 مرحباً بكم في بوت Farmton التلقائي")
    print("=" * 50)
    
    bot = FarmtonBot()
    bot.run_automation()

if __name__ == "__main__":
    main()
