import logging
import json

logger = logging.getLogger()
logger.setLevel('INFO')

settings = {
    'initial_file':'path/to/inital/file.txt',
    'encrypted_file':'path/to/encrypted/file.txt',
    'decrypted_file':'path/to/decrypted/file.txt',
    'symmetric_key':'path/to/symmetric/key.txt',
    'public_key':'path/to/public/key.pem',
    'secret_key':'path/to/secret/key.pem',
}

if __name__ == "__main__":
    try:
        with open('settings.json', 'w') as f:
            json.dump(settings, f)
        logging.info("Настройки записаны в файл!")
    except OSError as err:
        logging.warning(f'{err} ошибка при записи в файл {"settings.json"}!')