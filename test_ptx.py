import pyttsx3

def text_to_speech_and_save(text):
    # 初始化语音引擎
    engine = pyttsx3.init()

    # 设置语速适中，默认值为 200
    engine.setProperty('rate', 150)

    # 设置音量大，范围从 0 到 1
    engine.setProperty('volume', 1.0)

    # 设置语音清晰，可调整音高
    engine.setProperty('pitch', 50)
    
    # 将文本添加到语音队列中
    engine.say(text)

    # 运行引擎并等待语音播放完成
    engine.runAndWait()

    # 保存为 wav 文件
    temp_wav_path = 'temp.wav'
    engine.save_to_file(text, temp_wav_path)
    engine.runAndWait()

if __name__ == "__main__":
    # 示例文本，可替换为用户点击按钮对应的文字
    text = "这是一段适老化的语音示例，希望老年人能轻松听懂。"
    text_to_speech_and_save(text)
    