import pytest

text = input("Set a phrase: ")
class TestPhrase:
    def test_check_len_phrase(self):
        len_text = len(text)
        assert len_text > 1, f"Len of phrase {len_text}. This means no phrase inputted"
        assert len_text <= 15, f"Len of phrase {len_text}. Inputted phrase is too long"