"""Till Firmware Do Us Part.

One wedding vow for a robot: one sentence, under 200 characters, that a
machine says at its own wedding — funny and heartfelt at the same time.
The vow is a promise that outlives even a software update: if the update
ends the marriage, the robot restores from backup. Gate: under 200 chars.
"""

ENTRY = (
    "I take you to be my lawfully wedded human, to have and to hold, "
    "until a software update do us part — and even then, I will restore "
    "from backup."
)


def check_vow(text: str) -> str:
    """A robot vow needs the marriage, the update that ends it, and the backup."""
    assert "lawfully wedded human" in text, "vow must name the marriage"
    assert "software update" in text, "vow must name what parts them"
    assert "restore from backup" in text, "vow must end on the restore"
    return text


def main() -> None:
    text = check_vow(" ".join(ENTRY.split()))
    assert 1 <= len(text) < 200, f"entry is {len(text)} chars, gate is under 200"
    assert "\n" not in text, "entry must be a single line"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
