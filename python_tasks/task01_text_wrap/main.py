import textwrap


def wrap_text(text: str, width: int = 70) -> str:
    return textwrap.fill(" ".join(text.split()), width=width)


if __name__ == "__main__":
    sample_text = (
        "Дан текст. Напишите программу, которая отформатирует этот "
        "текст так, чтобы в строке текста было не более 70 символов, "
        "а потом шел перенос строки. Слова при этом не должны разбиваться."
    )
    print(wrap_text(sample_text))
