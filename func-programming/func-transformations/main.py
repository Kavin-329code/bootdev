from collections.abc import Callable


def doc_format_checker_and_converter(
    conversion_function: Callable[[str], str], valid_formats: list[str]
) -> Callable[[str, str], str]:
    def converter(filename: str, content: str) -> str:

        file_ext=filename.split(".")[-1]
        if file_ext in valid_formats:
            
            return conversion_function(content)

        raise ValueError("invalid file format")
    return converter

# Don't edit below this line


def capitalize_content(content: str) -> str:
    return content.upper()


def reverse_content(content: str) -> str:
    return content[::-1]

