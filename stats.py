def number_of_words(text):
    words = text.split()
    return len(words)
def num_unique_characters(text: str) -> dict[str, int]:
    unique_chars = set(text.lower())
    return {char: text.lower().count(char) for char in unique_chars}
def sort_on(char_count:tuple[str, int]) -> int:
    return char_count[1]
def chars_dict_to_sorted_list(char_count: dict[str, int]) -> list[tuple[str, int]]:
    return sorted(char_count.items(), key=sort_on, reverse=True)