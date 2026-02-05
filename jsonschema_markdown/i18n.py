from pathlib import Path

import i18n


LOCALE_DIR = Path(__file__).resolve().parent.parent / "locales"

i18n.set("file_format", "json")
i18n.set("filename_format", "{locale}.{format}")
i18n.set("skip_locale_root_data", True)
i18n.set("namespace_delimiter", "Do not use namespace delimiters")
i18n.load_path.append(LOCALE_DIR)


def set_locale(locale):
    """
    Update the current locale used for translating CLI output.

    Args:
        locale (str): The locale code to set.
    """
    i18n.set("locale", locale)


def gettext_with_locale(message):
    """
    Translate a message using the current locale.

    Args:
        message (str): The message to translate.

    Returns:
        str: The translated message.
    """
    try:
        return i18n.t(message)
    except Exception:
        return message


_ = gettext_with_locale
set_locale = set_locale
