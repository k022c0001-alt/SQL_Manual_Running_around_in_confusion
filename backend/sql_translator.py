import pytesseract
from PIL import Image
from google.cloud import translate_v2
import cv2
import numpy as np


class SQLImageTranslator:
    def __init__(self):
        self.translate_client = translate_v2.Client()

    def extract_text_from_image(self, image_data: bytes) -> str:
        """画像からテキストを抽出する"""
        nparr = np.frombuffer(image_data, np.uint8)
        # グレースケールで直接デコードしてノイズ除去
        gray = cv2.imdecode(nparr, cv2.IMREAD_GRAYSCALE)
        processed = cv2.medianBlur(gray, 3)

        # OCRで文字認識
        pil_image = Image.fromarray(processed)
        text = pytesseract.image_to_string(pil_image)
        return text.strip()

    def translate_text(self, text: str, target_language: str = "ja") -> str:
        """テキストを指定言語に翻訳する"""
        if not text:
            return ""
        response = self.translate_client.translate(
            text,
            target_language=target_language,
        )
        return response["translatedText"]

    def process(self, image_data: bytes, target_lang: str = "ja") -> dict:
        """画像からテキストを抽出して翻訳する"""
        sql_text = self.extract_text_from_image(image_data)
        translated = self.translate_text(sql_text, target_lang)
        return {
            "original": sql_text,
            "translated": translated,
            "language": target_lang,
        }
