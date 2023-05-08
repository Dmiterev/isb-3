import logging
import json

logger = logging.getLogger()
logger.setLevel('INFO')

settings = {
    'initial_file':'initial_file.txt',
    'encrypted_file': 'encrypted_file.txt',
    'decrypted_file': 'decrypted_file.txt',
    'symmetric_key': 'symmetric_key.txt',
    'public_key': 'public_key.pem',
    'secret_key': 'secret_key.pem',
}

if __name__ == "__main__":
    try:
        with open('settings.json', 'w') as f:
            json.dump(settings, f)
        logging.info("Настройки записаны в файл!")
    except OSError as err:
        logging.warning(f'{err} ошибка при записи в файл {"settings.json"}!')