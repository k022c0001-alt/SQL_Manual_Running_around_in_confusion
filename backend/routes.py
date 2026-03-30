import logging
from flask import Blueprint, request, jsonify

from backend.sql_translator import SQLImageTranslator

logger = logging.getLogger(__name__)

translator_bp = Blueprint("translator", __name__)

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif", "webp", "bmp"}

_translator = None


def get_translator() -> SQLImageTranslator:
    global _translator
    if _translator is None:
        _translator = SQLImageTranslator()
    return _translator


def allowed_file(filename: str) -> bool:
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    )


@translator_bp.route("/api/translate-image", methods=["POST"])
def translate_image():
    """画像をアップロードしてOCR・翻訳を行うエンドポイント"""
    if "file" not in request.files:
        return jsonify({"error": "ファイルがありません"}), 400

    file = request.files["file"]
    target_lang = request.form.get("language", "ja")

    if file.filename == "":
        return jsonify({"error": "ファイルが選択されていません"}), 400

    if not allowed_file(file.filename):
        return jsonify({"error": "サポートされていないファイル形式です"}), 400

    if target_lang not in ("ja", "en"):
        return jsonify({"error": "言語は 'ja' または 'en' を指定してください"}), 400

    try:
        image_data = file.read()
        result = get_translator().process(image_data, target_lang)
        return jsonify(result), 200
    except Exception as e:
        logger.exception("translate-image processing failed")
        return jsonify({"error": "画像の処理中にエラーが発生しました"}), 500
