# -*- coding: utf-8 -*-
from melo.api import TTS

# 语速
speed = 1.0
# 如果确定电脑有GPU支持cuda可直接写0
# 确定电脑没有GPU支持cuda直接写cpu
# 不确定有没有写auto，交给程序自行判断
device = 'auto' # or cuda:0

text = "Hello! 今天是 2024 年 10 月 15 日，天气晴朗。我们计划下午 3 点去外滩散步，然后在 Starbucks 喝一杯拿铁。记得带上雨伞哦，虽然天气预报说降水概率只有 20%，但还是小心为上！对了，别忘了明天早上要和 Alice 视频会议，讨论项目的 API 接口文档。加油，今天也要元气满满呀！"
model = TTS(language='ZH', device=device)
speaker_ids = model.hps.data.spk2id

output_path = 'test.mp3'
model.tts_to_file(text, speaker_ids['ZH'], output_path, speed=speed)
