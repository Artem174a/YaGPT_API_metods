import requests


class YaGPTException(Exception):
    pass


class YaGPT:
    def __init__(self, folder_id, iam_token):
        """
        Инициализация объекта LanguageModel.

        Parameters:
        - folder_id (str): Идентификатор каталога.
        - iam_token (str): IAM-токен.
        """
        self.folder_id = folder_id
        self.iam_token = iam_token
        self.api_url = "https://llm.api.cloud.yandex.net/llm/v1alpha/instruct"

    def instruct(self, model: str, instruction_text: str, request_text: str, max_tokens: int = 2500,
                 temperature: float = 0.8):
        """
        Отправка запроса к языковой модели.

        Parameters:
        - model (str): Языковая модель. Например, "general".
        - instruction_text (str): Предварительное текстовое условие для запроса.
        - request_text (str): Запрос, который должна выполнить нейросеть.
        - max_tokens (int): Максимальное количество токенов в сгенерированном тексте (по умолчанию 2500).
          Ограничивает суммарный размер входного и выходного текста.
        - temperature (float): Значение параметра температуры генерации (по умолчанию 0.8).
          Чем выше значение, тем более случайными будут ответы.

        Returns:
        - list or None: Список альтернативных результатов или None в случае ошибки.
        """
        try:
            payload = {
                "model": model,
                "instruction_text": instruction_text,
                "request_text": request_text,
                "generation_options": {
                    "max_tokens": max_tokens,
                    "temperature": temperature
                }
            }

            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.iam_token}",
                "x-folder-id": self.folder_id
            }

            response = requests.post(self.api_url, json=payload, headers=headers)

            response.raise_for_status()  # Проверка на ошибку HTTP-ответа

            result = response.json().get("result")
            if result and "alternatives" in result:
                return result["alternatives"]
            else:
                return None
        except requests.RequestException as e:
            # Обработка ошибок HTTP-запроса
            raise YaGPTException(f"Error during HTTP request: {e}")
        except Exception as e:
            # Общая обработка ошибок
            raise YaGPTException(f"Unexpected error: {e}")
