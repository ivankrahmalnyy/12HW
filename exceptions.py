class DataJsonError(Exception):
    """
    Обработка ошибки открытия json
    """
    pass

class WrongImgTypr(Exception):
    """
    Обработка ошибки загрузки файла не правильным расширением
    """
    pass